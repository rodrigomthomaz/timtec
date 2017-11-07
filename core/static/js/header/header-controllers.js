(function(angular){
    'use strict';
    var app = angular.module('header.controllers', ['ngCookies']);

    app.controller('HeaderCtrl', [
        '$scope',
        '$rootScope',
        '$interval',
        '$uibModal',
        '$cookieStore',
        'UserMessage',
        function ($scope, $rootScope, $interval, $uibModal, $cookieStore, UserMessage) {

            $scope.load_messages = function(){
                $scope.theres_new_messages = false;
                $scope.total_messages = 0;

                $scope.messages = UserMessage.query(function(data){
                    angular.forEach(data, function(message, key){
                        if (!message.is_read) {
                            $scope.theres_new_messages = true;
                            $scope.total_messages++;
                        }
                    })
                });
            };

            // loop to load
            $interval(function(){
                $scope.load_messages();
            }, 60 * 1000);
            $scope.load_messages();

            $scope.delete_message = function(msg) {
                msg.$delete(function(){
                    $scope.load_messages();
                });
            };

            if(window.LOAD_BANNER){
                var banner_showed = $cookieStore.get('banner_showed_' + window.USER_ID);
                if (!banner_showed){
                    var modalInstance = $uibModal.open({
                        templateUrl: 'banner.html',
                        controller: function($scope, $uibModalInstance){
                            $scope.cancel = function () {
                                $uibModalInstance.dismiss();
                            };
                        }
                    });
                    $cookieStore.put('banner_showed_' + window.USER_ID, true);
                }
            }

        }
    ]);

    app.controller('CourseHeaderCtrl', [
        '$scope',
        function ($scope) {
            $scope.confirmUrl = function(url, msg) {
                if (confirm(msg))
                    window.location.href = url;
            };
        }
    ]);

})(window.angular);
