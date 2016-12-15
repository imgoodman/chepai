function request(paras) {
    var url = location.href;  //获取当前url地址
    var paraString = url.substring(url.indexOf("?") + 1, url.length).split("&");
    var paraObj = {}
    for (i = 0; j = paraString[i]; i++) {
        paraObj[j.substring(0, j.indexOf("=")).toLowerCase()] = j.substring(j.indexOf("=") + 1, j.length);
    }
    var returnValue = paraObj[paras.toLowerCase()];
    if (typeof (returnValue) == "undefined") {
        return "";
    } else {
        return returnValue;
    }
};
function trimLastComma(str) {
    return str.substr(0, str.length - 1);
};
function showLongString(str, count) {
    if (str == "" || str == null)
        return "暂无";
    else {
        if (str.length > count) {
            return str.substr(0, count) + ".";
        } else {
            return str;
        }
    }
};
function showAxisName(axisid) {
    if (axisid == "1")
        return "X轴";
    else if (axisid == "2") {
        return "Y轴";
    } else {
        return "Z轴";
    }
};