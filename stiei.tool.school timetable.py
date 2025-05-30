import flask
import requests
cookies = {
    'GS_LTYPE': 'sso',
    'EMAP_LANG': 'zh',
    'THEME': 'teal',
    'GS_SESSIONID': '1b20cfcd02d21efc1dad7c4b8f36fef3',
    '_WEU': 'NCyd6n8c25WJWRhTGT1Nylza3eWy1BG_8tnXWzST5JXgGUVNe8O2j5SQ7tpTsF_BNOsK1u_S2QogtaLPeV7dZmUGXS38Q4IvnJxzmMukMdYa21UbCuzJZTK3KnV0W0GBFJoDpDWy0ud9q2Ww9ek5FCczLrVXihMIiRVDp*0wuymEeqnQBVkPSoc3pHuTHhqvyJMxOVPqVDT4XLclyeYhA3aBv0Jn1833GNyeIr*MQyQ50Wa*9VM63UW7jZ_FMoOjoBM6NdVn2_lmj93D1gCcq5RnmhtBkyn9kWk5k5t2jOS.',
    'arialoadData': 'false',
    'ariauseGraymode': 'false',
    'route': 'f35cd460aa58db03903c884b8a71bc32',
}
headers = {
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Fetch-Api': 'true',
    'Origin': 'https://jiaowunew.stiei.edu.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://jiaowunew.stiei.edu.cn/jwapp/sys/homeapp/home/index.html?av=1748566273038&contextPath=/jwapp',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
    'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'GS_LTYPE=sso; EMAP_LANG=zh; THEME=teal; GS_SESSIONID=1b20cfcd02d21efc1dad7c4b8f36fef3; _WEU=NCyd6n8c25WJWRhTGT1Nylza3eWy1BG_8tnXWzST5JXgGUVNe8O2j5SQ7tpTsF_BNOsK1u_S2QogtaLPeV7dZmUGXS38Q4IvnJxzmMukMdYa21UbCuzJZTK3KnV0W0GBFJoDpDWy0ud9q2Ww9ek5FCczLrVXihMIiRVDp*0wuymEeqnQBVkPSoc3pHuTHhqvyJMxOVPqVDT4XLclyeYhA3aBv0Jn1833GNyeIr*MQyQ50Wa*9VM63UW7jZ_FMoOjoBM6NdVn2_lmj93D1gCcq5RnmhtBkyn9kWk5k5t2jOS.; arialoadData=false; ariauseGraymode=false; route=f35cd460aa58db03903c884b8a71bc32',
}
data = {
    'termCode': '2024-2025-2',
    'campusCode': 'FX',
    'type': 'term',
}
response = requests.post(
    'https://jiaowunew.stiei.edu.cn/jwapp/sys/homeapp/api/home/student/getMyScheduleDetail.do',
    cookies=cookies,
    headers=headers,
    data=data,
).json()
print(response)
data = response
courses = data['datas']['arrangedList']

day_mapping = {
    1: '星期一',
    2: '星期二',
    3: '星期三',
    4: '星期四',
    5: '星期五',
    6: '星期六',
    7: '星期日'
}
for course in courses:
    name = course.get('courseName', '无课程名')
    day = day_mapping.get(course.get('dayOfWeek', 0), '未知')
    start = course.get('beginTime', '未知')
    end = course.get('endTime', '未知')
    place = course.get('placeName', '未知')
    teacher_info = course.get('weeksAndTeachers', '未知')

    if teacher_info != '未知':
        parts = teacher_info.split('/')
        weeks = parts[0].split('[')[0]
        teacher = parts[1].split('[')[0].strip()
    else:
        weeks = '未知'
        teacher = '未知'
    print(f"课程名称：{name}")
    print(f"上课时间：{day} {start} - {end}")
    print(f"上课地点：{place}")
    print(f"授课安排：{weeks}")
    print(f"授课教师：{teacher}")
