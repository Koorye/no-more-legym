__api__ = {
    "activities": {
        "url": "https://cpes.legym.cn/education/app/activity/getActivityList",
        "method": "post",
        "data": {"page": 1, "size": 50},
        "description": "获取活动列表",
    },
    "limit": {
        "url": "https://cpes.legym.cn/running/app/getRunningLimit",
        "method": "post",
        "data": {"semesterId": None},
        "description": "获取每日跑步里程上限",
    },
    "login": {
        "url": "https://cpes.legym.cn/authorization/user/manage/login",
        "method": "post",
        "data": {"entrance": "1", "password": None, "userName": None},
        "description": "登录乐健账号",
    },
    "register": {
        "url": "https://cpes.legym.cn/education/app/activity/signUp",
        "method": "post",
        "data": {"activityId": None},
        "description": "报名活动",
    },
    "running": {
        "url": "https://cpes.legym.cn/running/app/uploadRunningDetails",
        "method": "post",
        "data": {
            "scoringType": 1,
            "semesterId": None,
            "signPoint": [],
            "startTime": None,
            "totalMileage": None,
            "totalPart": 0.0,
            "type": "自由跑",
            "uneffectiveReason": "",
            "avePace": None,
            "calorie": None,
            "effectiveMileage": None,
            "effectivePart": 1,
            "endTime": None,
            "gpsMileage": None,
            "limitationsGoalsSexInfoId": None,
            "paceNumber": None,
            "paceRange": None,
            "routineLine": [
                {"latitude": 30.756303201239845, "longitude": 103.93206457325871},
                {"latitude": 30.756346614671184, "longitude": 103.93206545656531},
                {"latitude": 30.756359404607583, "longitude": 103.93407893568614},
                {"latitude": 30.753229499261558, "longitude": 103.93407611144278},
            ],
        },
        "description": "上传跑步数据",
    },
    "semester": {
        "url": "https://cpes.legym.cn/education/semester/getCurrent",
        "method": "get",
        "data": {},
        "description": "获取当前学期",
    },
    "sign": {
        "url": "https://cpes.legym.cn/education/activity/app/attainability/sign",
        "method": "put",
        "data": {
            "activityId": None,
            "times": "1",
            "pageType": "activity",
            "userId": None,
            "activityType": 0,
            "attainabilityType": 1,
        },
        "description": "签到活动",
    },
    "checkTimeInterval": {
        "url": "https://cpes.legym.cn/education/app/activity/checkSignInterval",
        "method": "get",
        "data": {"activityId": None},
        "description": "检查签到时间",
    }
}
