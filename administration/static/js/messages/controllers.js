(function(angular){
    'use strict';

    var module = angular.module('messages.controllers', ['ui.tinymce', 'ui.bootstrap']);

    // Service to share data across the controllers
    module.factory('messages_list', function() {
        return {
            messages : []
        };
    });

    module.controller('NewMessageController', ['$scope', '$interval', '$uibModal', '$window', 'Message', 'Student', 'StudentSearch', 'ClassSimple', 'messages_list', '$rootScope',
            function($scope, $interval, $uibModal, $window, Message, Student, StudentSearch, ClassSimple, messages_list, $rootScope) {
                $scope.course_id = parseInt($window.course_id, 10);
                $scope.messages = messages_list.messages;
                $scope.new_message = function () {
                    var modalInstance = $uibModal.open({
                        templateUrl: 'newMessageModal.html',
                        controller: ['$scope', '$uibModalInstance', 'course_id', SendMessageModalInstanceCtrl],
                        resolve: {
                            course_id: function () {
                                return $scope.course_id;
                            }
                        }
                    });
                };
                var SendMessageModalInstanceCtrl = function ($scope, $uibModalInstance, course_id) {

                    $scope.tinymceModel = 'Initial content';
                    $scope.tinymceOptions = {
                        resize: false,
                        menubar:false,
                        statusbar: false,

                        plugins: 'textcolor link',
                        toolbar: "undo redo styleselect bold italic forecolor backcolor link",
                    };

                    $scope.new_message = new Message();
                    $scope.new_message.course = course_id;
                    $scope.new_message.users = [];
                    $scope.recipient_list = [];
                    $scope.empty_msg_subject_error = false;
                    $scope.empty_msg_body_error = false;
                    $scope.sending = false;
                    $scope.progressbar_counter = 0;
                    $scope.specific_classes = [];

                    $scope.classes = ClassSimple.query({course: course_id}, function(classes){
                        classes.checked = [];
                        return classes;
                    });

                    // trick to user modal.all_checked in ng-model html tag
                    $scope.modal = {};
                    $scope.modal.all_checked = true;

                    $scope.send = function () {

                        // progressbar
                        $interval(function(){
                            if($scope.progressbar_counter == 0){
                                $scope.progressbar_counter = 20;
                            }
                            $scope.progressbar_counter++;
                        },1000,0);

                        // TODO validação dos campo: títle e message não podem ser vazios
                        if ($scope.modal.all_checked) {
                            $scope.new_message.users = [];
                            angular.forEach($scope.classes, function(klass) {
                                angular.forEach(klass.students, function(student) {
                                    $scope.new_message.users = $scope.new_message.users.concat(student);
                                });
                            });
                        } else if ($scope.specific_classes.length > 0) {
                            angular.forEach($scope.specific_classes, function(klass) {
                                angular.forEach(klass.students, function(student) {
                                    $scope.new_message.users = $scope.new_message.users.concat(student);
                                });
                            });
                        }
                        if ($scope.new_message.message && $scope.new_message.subject) {
                            $scope.sending = true;
                            $scope.new_message.$save({}, function(new_message){
                                messages_list.messages.unshift(new_message);
                                $scope.progressbar_counter = 100;
                                $rootScope.$broadcast('newMessage');
                                $scope.sending = false;
                                $uibModalInstance.close();
                            });
                            $scope.empty_msg_subject_error = false;
                            $scope.empty_msg_body_error = false;
                        }
                        if (!$scope.new_message.message) {
                            $scope.empty_msg_body_error = true;
                        } else {
                            $scope.empty_msg_body_error = false;
                        }
                        if (!$scope.new_message.subject) {
                            $scope.empty_msg_subject_error = true;
                        } else {
                            $scope.empty_msg_subject_error = false;
                        }
                    };

                    $scope.cancel = function () {
                        $uibModalInstance.dismiss();
                    };
                    $scope.getUsers = function(val) {
                        return new StudentSearch(val, course_id);
                    };

                    $scope.on_select_student = function(model) {
                        $scope.new_message.users.unshift(model.id);
                        $scope.recipient_list.unshift(model);
                        $scope.asyncSelected = '';
                    };

                    $scope.remove_student = function(index) {
                        $scope.new_message.users.splice(index, 1);
                        $scope.recipient_list.splice(index, 1);
                    };

                };
            }
        ]);

    module.controller('MessagesListController', ['$scope', '$uibModal', '$window', 'Message', 'messages_list',
        function($scope, $uibModal, $window, Message, messages_list) {
            $scope.USER_ID = parseInt(window.USER_ID);
            $scope.course_id = parseInt($window.course_id, 10);
            $scope.course_slug = $window.course_slug;
            messages_list.messages = Message.query({course: $scope.course_id});
            $scope.messages = messages_list.messages;
            $scope.$on('newMessage', function() {
                $scope.messages = messages_list.messages;
            });
        }
    ]);

    module.controller('MessageController', ['$scope', '$window', 'Message', 'AnswerMessage',
        function($scope, $window, Message, AnswerMessage) {
            $scope.course_id = parseInt($window.course_id, 10);
            $scope.message_id = document.location.href.match(/message\/([0-9]+)/)[1];
            $scope.message = Message.get({messageId: $scope.message_id}, function(message) {console.log(message)});

            $scope.show_recipients = false;
            $scope.toggle_recipient_list = function(){
                $scope.show_recipients = !$scope.show_recipients;
            };

            $scope.answer_message = function(){

                var answer_message = new AnswerMessage({
                    user: window.USER_ID,
                    message: $scope.message.id,
                    text: $scope.new_answer
                });

                answer_message.$save(function(m){
                    $scope.message.answers.push(m);
                    $scope.new_answer = '';
                });

            };

            $scope.answer_as_new_message = function(){
                if (window.USER_ID == $scope.message.professor.id){
                    $scope.answer_message();
                    return;
                }
                var msg_date = new Date($scope.message.date);
                msg_date = msg_date.getDate() + '/' + (msg_date.getMonth() + 1) + '/' + msg_date.getFullYear() + ' ' + msg_date.getHours() + ':' + msg_date.getMinutes();
                var answer_as_new_message = new Message({
                    course: $scope.course_id,
                    users: [$scope.message.professor.id, window.USER_ID],
                    subject: 'RE: '+ $scope.message.subject,
                    message: '<blockquote>'
                                + $scope.message.message
                                + '<p>'
                                + 'Enviado em ' + msg_date
                                + '</p>'
                            + '</blockquote><br />' + $scope.new_answer
                });
                answer_as_new_message.$save(
                    function(m){
                        window.location.href = m.get_absolute_url
                    }
                );
            };
        }
    ]);

    module.controller('AllMessagesController', ['$scope', 'UserAllMessages', 'Message', 'AnswerMessage',
        function($scope, UserAllMessages, Message, AnswerMessage) {
            $scope.loading_messages = true;

            $scope.load_messages = function(){
                $scope.messages = UserAllMessages.query({'q': $scope.query}, function(msgs){
                    $scope.loading_messages = false;
                });
            };

            $scope.load_messages();

            $scope.show_message = function(msg) {
                $scope.showing_message = msg;
                Message.get({messageId: msg.id}, function() {
                    msg.is_read = true;
                });
            };

            $scope.hide_message = function() {
                delete $scope.showing_message;
            };

            $scope.delete_message = function(){
                var params = {messageId: $scope.showing_message.id};
                // permanent delete, because is deleting from trash
                if ($scope.filter_trash)
                    params.perma = '1';
                Message.delete(params, function(){
                    $scope.messages.splice($scope.messages.indexOf($scope.showing_message), 1);
                    $scope.hide_message();
                });
            };

            $scope.answer_message = function(){

                var answer_message = new AnswerMessage({
                    user: window.USER_ID,
                    message: $scope.showing_message.id,
                    text: $scope.new_answer
                });

                answer_message.$save(function(m){
                    $scope.showing_message.answers.push(m);
                    $scope.new_answer = '';
                }, function (e){
                    console.log(e);
                });

            };

            $scope.answer_as_new_message = function(){
                if (window.USER_ID == $scope.showing_message.professor.id){
                    $scope.answer_message();
                    return;
                }
                var msg_date = new Date($scope.showing_message.date);
                msg_date = msg_date.getDate() + '/' + (msg_date.getMonth() + 1) + '/' + msg_date.getFullYear() + ' ' + msg_date.getHours() + ':' + msg_date.getMinutes();
                var answer_as_new_message = new Message({
                    course: null,
                    users: [$scope.showing_message.professor.id, window.USER_ID],
                    subject: 'RE: '+ $scope.showing_message.subject,
                    message: '<blockquote>'
                                + $scope.showing_message.message
                                + '<p>'
                                + 'Enviado em ' + msg_date
                                + '</p>'
                            + '</blockquote><br />' + $scope.new_answer
                });
                answer_as_new_message.$save(
                    function(m){
                        $scope.messsages.push(m);
                        $scope.show_message(m);
                    }
                );
            };

            $scope.toggle_message = function(msg){
                msg.checked = !msg.checked;
            };

            $scope.toggle_all = function(){
                $scope.messages = $scope.messages.map(function(message){
                    message.checked = $scope.checked_all;
                    return message;
                });
            };

            $scope.select_all = function(){
                $scope.checked_all = true;
                $scope.toggle_all();
            };

            $scope.select_read = function(){
                $scope.checked_all = true;
                $scope.messages = $scope.messages.map(function(message){
                    message.checked = message.is_read;
                    return message;
                });
            };

            $scope.select_unread = function(){
                $scope.checked_all = true;
                $scope.messages = $scope.messages.map(function(message){
                    message.checked = !message.is_read;
                    return message;
                });
            };

            $scope.select_message = function(checked){
                if (checked)
                    $scope.checked_all = true;
                else {
                    var checked = false;
                    angular.forEach($scope.messages, function(message){
                        if (!checked && message.checked)
                            checked = true;
                    });
                    if (!checked)
                        $scope.checked_all = false;
                }

            };

            $scope.delete_selected = function() {
                var params = {messageId: message.id};
                // permanent delete, because is deleting from trash
                if ($scope.filter_trash)
                    params.perma = '1';

                angular.forEach($scope.messages, function(message){
                    if (message.checked)
                        Message.delete(params);

                });

                $scope.messages = $scope.messages.filter(function(message) {
                    return !message.checked;
                });

                $scope.checked_all = false;
            };

            $scope.filter_inbox = function(){
                if($scope.inbox_filter) return;
                $scope.hide_message();
                $scope.inbox_filter = true;
                $scope.sent_filter = false;
                $scope.trash_filter = false;
                $scope.load_messages();
            };

            $scope.filter_sent = function(){
                if($scope.sent_filter) return;
                $scope.hide_message();
                $scope.inbox_filter = false;
                $scope.sent_filter = true;
                $scope.trash_filter = false;
                $scope.messages = $scope.messages.filter(function(message){

                });
            };

            $scope.filter_trash = function(){
                if($scope.trash_filter) return;
                $scope.hide_message();
                $scope.inbox_filter = false;
                $scope.sent_filter = false;
                $scope.trash_filter = true;
                $scope.loading_messages = true;
                $scope.messages = UserAllMessages.query({'q': $scope.query, 'trash': '1'}, function(msgs){
                    $scope.loading_messages = false;
                });
            };

        }
    ]);

})(angular);
