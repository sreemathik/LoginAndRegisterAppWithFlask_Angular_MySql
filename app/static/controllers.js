
angular.module('myApp').controller('loginController',
['$scope', '$location', 'AuthService',
function ($scope, $location, AuthService) {

  $scope.login = function () {

    $scope.error = false;
    $scope.disabled = true;

    AuthService.login($scope.loginForm.email, $scope.loginForm.password)
      .then(function (response) {
        localStorage.setItem('token', response.data.auth_token); 
        $location.path('/');
        $scope.disabled = false;
        $scope.loginForm = {};
      })
      .catch(function () {
        $scope.error = true;
        $scope.errorMessage = "Invalid username and/or password";
        $scope.disabled = false;
        $scope.loginForm = {};
      });

  };

}]);

angular.module('myApp').controller('logoutController',
['$scope', '$location',
function ($scope, $location) {

  $scope.logout = function () {
    localStorage.removeItem('token'); 
    $location.path('/login');
  };

}]);

angular.module('myApp').controller('registerController',
['$scope', '$location', 'AuthService',
function ($scope, $location, AuthService) {

  $scope.register = function () {

    $scope.error = false;
    $scope.disabled = true;

    AuthService.register($scope.registerForm.email,
                         $scope.registerForm.password)
      .then(function (response) {
        localStorage.setItem('token', response.data.auth_token); 
        $location.path('/login');
        $scope.disabled = false;
        $scope.registerForm = {};
      })
      .catch(function () {
        $scope.error = true;
        $scope.errorMessage = "Something went wrong!";
        $scope.disabled = false;
        $scope.registerForm = {};
      });

  };

}]);
