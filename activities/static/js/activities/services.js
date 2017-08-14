(function(angular){
    'use strict';

    angular.module('activities.services', ['ngRoute', 'ngResource']).
        factory('ActivityImage', function($resource){
            return $resource('/api/activity_image/:id/', {}, {
                update: {method: 'PUT'}
            });
        });
})(angular);
