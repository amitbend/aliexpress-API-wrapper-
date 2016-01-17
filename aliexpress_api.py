from urllib2 import Request, urlopen, URLError
import simplejson

commissionRateFrom = 0.04
commissionRateTo = 0.9
# pagesize max value = 40
pageSize = 40

def listPromotionProduct(appkey,fields=[],keywords=[]):
	fieldString = ",".join(fields)
	keywordString = ",".join(keywords)

	requestString = "http://gw.api.alibaba.com/openapi/param2/2/portals.open/api.listPromotionProduct/" + appkey + "?fields="+ fieldString + "&keywords=" + keywordString

	try:
		response = urlopen(requestString).read()
		r = simplejson.loads(response)
		errorCode = r['errorCode']
		if errorCode == 20010000:
			print 'call success'
		else:
			print 'call failure number :' + str()
		return [errorCode,r['result']['products'],r['result']['totalResults'] ]
		#print response
	except URLError, e:
	    print 'Had a url error says: ', e
	    return


	
def getPromotionProductDetail(appkey,fields=[],productId='0'):
	fieldString = ",".join(fields)

	requestString = "http://gw.api.alibaba.com/openapi/param2/2/portals.open/api.getPromotionProductDetail/" + appkey +"?fields=" + fieldString + "&productId=" + productId

	try:
		response = urlopen(requestString).read()
		r = simplejson.loads(response)
		print r
		errorCode = r['errorCode']
		if errorCode == 20010000:
			print 'call success'
		else:
			print 'call failure number :' + str()
		return [errorCode,r['result'] ]
		#print response
	except URLError, e:
	    print 'Had a url error says: ', e
	    return


def getPromotionLinks(appkey,fields=[],trackingID='0',urls=['']):
	# limit for urls converted in a call = 50
	if len(urls) > 50:
		print "Too many urls to convert, the limit is 50"
		return
	fieldString = ",".join(fields)
	requestUrls = ",".join(urls)
	requestString = "http://gw.api.alibaba.com/openapi/param2/2/portals.open/api.getPromotionLinks/" + appkey + "?fields=" +fieldString + "&trackingId=" +trackingID + "&urls=" +requestUrls
	print requestString
	try:
		response = urlopen(requestString).read()
		r = simplejson.loads(response)
		errorCode = r['errorCode']
		if errorCode == 20010000:
			print 'call success'
		else:
			print "we found an error: " + str(errorCode)
			print r
			return

		return [errorCode,r['result'] ]
		#print response
	except URLError, e:
	    print 'Had a url error says: ', e
	    return

	return

def main(): 
	# add your details
	appkey = ''
	trackingID = ''

	promoProductResult = listPromotionProduct(appkey,["totalResults","productId","productTitle","originalPrice","salePrice","discount"],["led","solar"])
	print promoProductResult
	fields2 = ['productId','productTitle','productUrl','imageUrl','originalPrice','salePrice','discount','evaluateScore','commission','commissionRate','30daysCommission','volume','packageType','lotNum','validTime','storeName','storeUrl']
	productId = '32220177784'
	PromotionProductDetailResult = getPromotionProductDetail(appkey,fields2,productId)
	print PromotionProductDetailResult
	fields3 = ['totalResults','trackingId','publisherId','url','promotionUrl']
	urls = ['http://www.aliexpress.com/item//852517607.html']
	getPromotionLinksResult = getPromotionLinks(appkey,fields3,trackingID,urls)
	print getPromotionLinksResult
main()
