var NGINX_PRE = '';
var API_ROOT = "http://"+window.location.host+"/"+NGINX_PRE+"api/";

var API = {
    instance: API_ROOT+"instance/",
    token: API_ROOT+"token/",
    location: API_ROOT+"location/",
    dataset: API_ROOT+"dataset/",
    group: API_ROOT+"group/",
    livecheck: API_ROOT+"livecheck"
}
