(function(angular){
    'use strict';

    angular.module('activities', [
        'django',
        'activities.controllers',
        'activities.directives',
        'activities.services',
        'ui.bootstrap',
        'ui.codemirror',
        'header'
    ]);
})(angular);
