odoo.define('most_sold_viewed.dynamic', function (require) {
   var PublicWidget = require('web.public.widget');
   var rpc = require('web.rpc');
   var core = require('web.core');
   var Qweb = core.qweb;
   var Dynamic = PublicWidget.Widget.extend({
       selector: '.dynamic_snippet_most_sold_viewed',
       start: function () {
       console.log('ssssss')
           var self = this;
           rpc.query({
               route: '/most_sold',
               params: {},
           }).then(function (result) {
           sold = result
            sold[0].set_active = true;
            $('.qweb_most_sold_viewed').append(Qweb.render('most_sold_viewed.product_sold', {sold}));
           });


            rpc.query({
               route: '/most_viewed',
               params: {},
           })
                .then(function (result) {
                viewed = result
            result[0].set_active = true;
            $('.qweb_most_sold_viewed').append(Qweb.render('most_sold_viewed.product_viewed', {viewed}));
           });
       },
   });
   PublicWidget.registry.dynamic_snippet_most_sold_viewed = Dynamic;
   return Dynamic;
});