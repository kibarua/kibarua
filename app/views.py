from flask import Blueprint , jsonify , request

from . import db 

from . models import Service , User , Client , Task

from . utils  import get_unique_id , on_finish, get_client_sms ,get_contractor_sms

import africastalking

sms = africastalking.SMS

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/' , methods=['POST', 'GET'])
def services_view():
    if request. method == 'POST':
        # TODO check if user is authenticated
        data = request.get_json()
        # TODO validate data
        name = data['name']
        photo = data['photo']
        cost = data['cost']

        service = Service(name=name, photo=photo, cost=cost)

        service.save()

        return  jsonify({'message':'Service created'}) , 201
    services_query  = Service.query.all()
    services = [service.to_dict() for service in  services_query]
    
    return jsonify({'services':services})


@api.route('/check_location')
def check_location():
    location  = request.args.get('loc')

    print(location)
    users_available = User.query.filter(User.location == location).first()

    print(users_available)
    if users_available:
        return jsonify({'available':True})
    return jsonify({'available':False})


@api.route('/add_client' , methods=['POST'])
def add_client():

    data = request.get_json()

    name = data['name']
    location  =  data['location']
    service_id = data['service']
    phone = data['phone']
    national_id = data['national_id']
    new_user = User(name=name , location=location , service_id = service_id , phone=phone , national_id=national_id)

    new_user.save()

    return jsonify({"message":"Created , wait for response"}) , 201


@api.route('/add_task', methods=['POST'])
def order_service():
    data = request.get_json()
    
    # TODO Validate
    client_phone = data['phone'] 
    # Validate phone

    service_id  = data['service_id']
    location = data['location']

    client = Client(name='Unknown' , phone=client_phone)
    client.save()

    # THE code to do this is complicated 
    # TODO look at this when u are okay make it random
    contractor  = User.query.filter(User.location == location).first()


    task = Task(employer_id = contractor.id, 
                client_id = client.id , 
                service_id=service_id ,
                task_id = str(get_unique_id(contractor.id)))
    task.save()
    # client sms
    client_template = get_client_sms(contractor , task)
    sms.send(client_template ,[client.phone],callback=on_finish)


    contractor_template = get_contractor_sms(contractor,task)
    sms.send(contractor_template ,[contractor.phone],callback=on_finish)
    return jsonify()