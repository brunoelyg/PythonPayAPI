(function() {
    'use strict';

    angular
        .module('app', [])
        .factory('ApiService', ApiService)
        .controller('ApiController', ApiController)

    function ApiController(ApiService){
        var vm = this;
        vm.form = {
            api_key: '',
            secret_key: ''
        }
        vm.getApi = getApi

        function getApi(){
            ApiService.get(vm.form.api_key, vm.form.secret_key).then(
                cbOk,
                cbError
            )

            function cbOk(response){
                vm.response = response;
            }

            function cbError(error){
                console.log(error)
            }
        }
    }

    function ApiService($q, $http){
        var model = {
            get: get,
        }

        return model;

        function get(api_key, secret_key){
            var deferred = $q.defer();
            var nonce = generate_nonce(10);
            var signature = generate_hash(nonce, api_key, secret_key);
            var header = {
                    headers: {
                        'Key': api_key,
                        'Signature': signature,
                        'Nonce': nonce,
                    }
                }
            

            $http
                .post('https://www.bitcointoyou.com/Payments/getInvoices.aspx', {}, header)
                .then(
                    cbOk,
                    cbError,
                )

            return deferred.promise;

            function cbOk(response){
                deferred.resolve(response.data)
            }

            function cbError(error){
                deferred.reject(error)
            }
        }

        function generate_nonce(length) {
            var text = "";
            var possible = "0123456789";
            for(var i = 0; i < length; i++) {
                text += possible.charAt(Math.floor(Math.random() * possible.length));
            }
            return text;
        }

        function generate_hash(nonce, api_key, secret_key){
            var hash = CryptoJS.HmacSHA256(nonce + secret_key, api_key);
            return CryptoJS.enc.Base64.stringify(hash);
        }
    }
})();