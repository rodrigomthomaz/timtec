(function (angular) {
    'use strict';

    var app = angular.module('courseMaterial.controllers', ['ngCookies']);

    app.controller('CourseMaterialEditorCtrl', ['$scope', '$window', 'CourseMaterial','CourseMaterialFile',
        function ($scope, $window, CourseMaterial, CourseMaterialFile) {
            $scope.courseId = $window.course_id;

            $scope.course_materials = CourseMaterial.query({course__id: $scope.courseId}, function (course_materials){
                if(course_materials.length === 1) {
                    $scope.course_material = course_materials[0];
                }
            });

            $scope.save_course_material = function(){
                $scope.course_material.$update({course: $scope.courseId}, function(){
                    $scope.alert.success('Alterações salvas com sucesso!');
                });
            };

            $scope.delete_file = function(file_obj){
                if (confirm('Tem certeza que dejeja apagar este arquivo?')){
                    CourseMaterialFile.delete({id: file_obj.id}, function(){
                        angular.forEach($scope.course_material.files, function(file, index){
                            if (file.id == file_obj.id){
                                $scope.course_material.files.splice(index, 1);
                                $scope.alert.success('Arquivo removido com sucesso!');
                            }
                        });
                    });
                }
            };
            $scope.hiden_file = function(file_obj){
                // console.log($scope.course_material);
                angular.forEach($scope.course_material.files, function(file, index){
                    if (file.id == file_obj.id){
                        file.hide = !file.hide;
                        $scope.course_material.files[index].hide = !$scope.course_material.files[index].hide;
                        var file_post = CourseMaterialFile.query({id: file_obj.id}, function(a){
                            console.log(a);
                        });
                        console.log(file_post);
                        file_post.hide = file.hide;
                        file_post.$update();
                        file_post.$update({id: file.id}, function(a){
                            console.log(a);
                        });
                    }
                });
            };
    }]);
})(angular);
