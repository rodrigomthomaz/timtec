
(function (angular) {
    'use strict';

    var module = angular.module('messages.services', ['ngRoute', 'ngResource']);
    module.factory('Message', function($resource){
            return $resource('/api/professor_message/:messageId', {}, {
                update: {method: 'PUT'}
            });
    });

    module.factory('User', function($resource){
            return $resource('/api/user/:userId', {}, {
            });
    });

    module.factory('Student', function($resource){
            return $resource('/api/course_student/', {}, {});
    });

    module.factory('AnswerMessage', function($resource){
        return $resource('/api/message_answer', {}, {});
    });

    module.factory('UserAllMessages', function($resource){
        return $resource('/api/user_all_messages', {}, {});
    });

})(angular);
