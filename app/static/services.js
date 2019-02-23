angular.module('myApp').factory('AuthService',
  ['$http',
  function ($http) {

    return ({
      login: login,
      register: register,
      isAuthenticated: isAuthenticated
    });

    var headers = {'Content-Type': 'application/json'};

    function login(email, password) {
       return $http.post('/api/login', {email: email, password: password}, {headers: headers});
    }

    function register(name, email, password) {
       return $http.post('/api/register', {name: name, email: email, password: password}, {headers: headers});
    }

    function isAuthenticated() {
        var token = localStorage.getItem('token');
        var headerWithAuthToken = {
            'Content-Type': 'application/json',
             Authorization: `Bearer ${token}`
          };
    
        return $http.get('/api/status', {headers: headerWithAuthToken});
    }

}]);