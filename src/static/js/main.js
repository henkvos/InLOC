var InLOC = angular.module('InLOC', []);

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
                //template:'<h3>hoi hoi</h3>'
                //controller: 'MainCtrl'
            }

        ).otherwise(
            {
                template:'something else'
            }
            )
    }
);