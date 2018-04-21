import random



def get_unique_id(id):
    
    return ''.join(random.choice(string.ascii_uppercase) for x in range(4))+id
     

def on_finish(error, response):
    if error is not None:
        raise error
    print('Sent')
    print(response)


def get_client_sms(contractor , task):

    return '''Hello client \n 
        We have found a contactor for you.
        Here are the details \n
        Contactor Name :{} \n
        Number:{} \n
        Cost:{} \n
        TaskID:{}
        '''.format(contractor.name,
                contractor.phone, 300 , task.task_id)


def get_contractor_sms(contractor , task):
     return '''Hello {} \n 
        We have found a job for you.
        Here are the details \n
        Contactor Name :{} \n
        TaskID:{}
        '''.format(contractor.name,
                contractor.phone , task.task_id)