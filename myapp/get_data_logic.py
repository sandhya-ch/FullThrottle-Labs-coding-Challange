from .models import User_details,ActivityPeriod
def data_get():
    final_data = {
        "ok":"true"
    }
    data=User_details.objects.all()
    members=[]
    for row in data:
        id=row.user_id
        real_name=row.real_name
        tz=row.tz
        single_data={'id':id, 'real_name':real_name, 'tz':tz}
        activity_data=ActivityPeriod.objects.filter(user=row.id)
        activity_periods = []
        for column in activity_data:
            start_time = column.start_time
            end_time = column.end_time
            time_data = {'start_time':start_time,"end_time":end_time}
            activity_periods.append(time_data)
        single_data.update({'activity_periods':activity_periods})
        members.append(single_data)
    final_data.update({'members':members})
    return final_data