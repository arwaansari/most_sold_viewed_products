from odoo import http
from odoo.http import request


class MostSold(http.Controller):
    @http.route(['/most_sold'], type="json", auth="public")
    def most_sold(self):
        sale_order = request.env['sale.order'].sudo().search([
            ('state', 'in', ['sale', 'done'])])
        product_list = []
        for rec in sale_order:
            total_sold = rec.order_line.mapped('product_template_id')
            print('ttll', total_sold)
            [product_list.append(i) for i in total_sold]
        print(product_list)
        product_count = {}
        for i in product_list:
            if i in product_count:
                product_count[i] += 1
            else:
                product_count[i] = 1
        sorted_product_count = dict(sorted(product_count.items(),
                                    key=lambda x: x[1], reverse=True))
        li = [[i.name, i.id] for i in sorted_product_count]
        new_list = [li[i:i + 4] for i in range(0, len(li), 4)]
        print('new', new_list)
        return new_list

    @http.route(['/most_viewed'], type="json", auth="public")
    def most_viewed(self):
        website_products = request.env['website.track'].sudo().search([]).\
            filtered(lambda l: l.product_id).product_id
        values = [[rec.name, rec.product_tmpl_id.id] for rec in website_products]
        new_list = [values[i:i + 4] for i in range(0, len(values), 4)]
        print(new_list)
        return new_list





