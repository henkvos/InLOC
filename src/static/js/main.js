var InLOC = angular.module('InLOC', []);

InLOC.config(function ($routeProvider){
        $routeProvider.when('/',
            {
                templateUrl:'/static/partials/home.html'
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