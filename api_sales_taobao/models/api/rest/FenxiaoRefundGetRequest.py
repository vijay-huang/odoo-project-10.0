'''
Created by auto_sdk on 2016.04.14
'''
from base import RestApi
class FenxiaoRefundGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.query_seller_refund = None
		self.sub_order_id = None

	def getapiname(self):
		return 'taobao.fenxiao.refund.get'
