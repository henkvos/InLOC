var InLOC = angular.module('InLOC', ['ui']);


function LOCStructureListController($scope, $http) {

    $http.get('/api/locstructures/').success(function(data) {
        $scope.locstructures = data;
    });

}

function LOCStructureDetailController($scope, $http, $routeParams) {
    var pkId = $routeParams.pk_id;
    console.log(pkId);
    $http.get('/api/locstructures/'+pkId).success(function(data) {
        $scope.locstructure = data;
    });

}

InLOC.config(function ($routeProvider){
        $routeProvider.when('/',
            {
                templateUrl:'/partials/start'
                //template:'<h3>hoi hoi</h3>'
                //controller: 'MainCtrl'
            }
        ).when('/loc/import',
            {
                templateUrl:'/partials/import'

            }

        ).when('/loc/add',
            {
                templateUrl:'/partials/locstructure/add'

            }

        ).when('/locstructure/:pk_id',
            {
                templateUrl:'/partials/locstructure',
                controller: 'LOCStructureDetailController'
            }

        ).otherwise(
            {
                template:'something else'
            }
            )
    }
);
