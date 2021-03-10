def uavsar_info():
    uavsar = [
    # Query 1
    {
    'q_num':'1',
    'reference_image':'uavsar_query1_reference.tiff',
    'request_url':'Band1/coverage/rangeset?subset=lat(63.7:64.1)&subset=lon(-145.9:-145.7)&format=image%2Ftiff&granuleID=',
    'message':'Variable subset Band1. Spatial subset',
    'prod_gid':'G1422449017-ASF',
    'uat_gid':'G1233284367-ASF',
    'sit_gid':'G1233284367-ASF',
    'outfile':'_uavsar_query1.tiff',
    'cs': 'Geographic',
    'proj_cs':'NA',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': 'NA',
    'gcs_epsg': '4326',
    'subset': [63.7, 64.1, -145.9, -145.7],
    'bands': 1,
    'variables': ['Band1', 'NA', 'NA', 'NA'],
    'xy_size':[1800, 7200]
    },
    # Query 2
    {
    'q_num':'2',
    'reference_image':'uavsar_query2_reference.tiff',
    'request_url':'Band2/coverage/rangeset?subset=lat(63.75:64.1)&subset=lon(-146.07:-145.8)&format=image%2Ftiff&granuleID=',
    'message':'Variable subset Band2. Spatial subset',
    'prod_gid':'G1422449017-ASF',
    'uat_gid':'G1233284367-ASF',
    'sit_gid':'G1233284367-ASF',
    'outfile':'_uavsar_query2.tiff',
    'cs': 'Geographic',
    'proj_cs':'NA',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': 'NA',
    'gcs_epsg': '4326',
    'subset': [63.75, 64.1, -146.07, -145.8],
    'bands': 1,
    'variables': ['Band2', 'NA', 'NA', 'NA'],
    'xy_size':[2430, 6300]
    },
    # Query 3
    {
    'q_num':'3',
    'reference_image':'uavsar_query3_reference.tiff',
    'request_url':'Band3/coverage/rangeset?subset=lat(63.85:64.15)&subset=lon(-145.9:-145.8)&format=image%2Ftiff&granuleID=',
    'message':'Variable subset Band3. Spatial subset',
    'prod_gid':'G1422449017-ASF',
    'uat_gid':'G1233284367-ASF',
    'sit_gid':'G1233284367-ASF',
    'outfile':'_uavsar_query3.tiff',
    'cs': 'Geographic',
    'proj_cs':'NA',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': 'NA',
    'gcs_epsg': '4326',
    'subset': [63.85, 64.15, -145.9, -145.8],
    'bands': 1,
    'variables': ['Band3', 'NA', 'NA', 'NA'],
    'xy_size':[900, 5400]
    },
    # Query 4
    {
    'q_num':'4',
    'reference_image':'uavsar_query4_reference.tiff',
    'request_url':'Band1%2CBand2/coverage/rangeset?subset=lat(40.05:40.06)&subset=lon(-123.39:-123.34)&format=image%2Ftiff&granuleID=',
    'message':'Variable subset 2 bands (1 & 2). Spatial subset.',
    'prod_gid':'G1366089385-ASF',
    'uat_gid':'G1233284371-ASF',
    'sit_gid':'G1233284371-ASF',
    'outfile':'_uavsar_query4.tiff',
    'cs': 'Geographic',
    'proj_cs':'NA',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': 'NA',
    'gcs_epsg': '4326',
    'subset': [40.05, 40.06, -123.39, -123.34],
    'bands': 2,
    'variables': ['Band1', 'Band2', 'NA', 'NA'],
    'xy_size':[900, 180]
    },
    # Query 5
    {
    'q_num':'5',
    'reference_image':'uavsar_query5_reference.tiff',
    'request_url':'all/coverage/rangeset?subset=lat(39.95:40.0)&subset=lon(-123.69:-123.59)&format=image%2Ftiff&granuleID=',
    'message':'Variable subset 3 bands using "all". Spatial subset.',
    'prod_gid':'G1366089385-ASF',
    'uat_gid':'G1233284371-ASF',
    'sit_gid':'G1233284371-ASF',
    'outfile':'_uavsar_query5.tiff',
    'cs': 'Geographic',
    'proj_cs':'NA',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': 'NA',
    'gcs_epsg': '4326',
    'subset': [39.95, 40.0, -123.69, -123.59],
    'bands': 3,
    'variables': ['Band1', 'Band2', 'Band3', 'NA'],
    'xy_size':[1800, 900]
    },
    #Query 6
    {
    'q_num':'6',
    'reference_image':'uavsar_query6_reference.tiff',
    'request_url':'all/coverage/rangeset?subset=lat(-0.034:0.09)&subset=lon(11.57:11.6)&format=image%2Ftiff&granuleID=',
    'message':'Spatial subset across the equator. All 3 bands',
    'prod_gid':'G1232482059-ASF',
    'uat_gid':'G1233284343-ASF',
    'sit_gid':'G1233284343-ASF',
    'outfile':'_uavsar_query6.tiff',
    'cs': 'Geographic',
    'proj_cs':'NA',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': 'NA',
    'gcs_epsg': '4326',
    'subset': [-.03, 0.09, 11.57, 11.6],
    'bands': 3,
    'variables': ['Band1', 'Band2', 'Band3', 'NA'],
    'xy_size':[540, 2232]
    },
    # Query 7
    {
    'q_num':'7',
    'reference_image':'uavsar_query7_reference.tiff',
    'request_url':'all/coverage/rangeset?subset=lat(61:62)&subset=lon(-139:-137)&format=image%2Ftiff&granuleID=',
    'message':'Northern hemisphere and subset bbox larger than granule extent.',
    'prod_gid':'G1402334529-ASF',
    'uat_gid':'G1233284396-ASF',
    'sit_gid':'G1233284396-ASF',
    'outfile':'_uavsar_query7.tiff',
    'cs': 'Geographic',
    'proj_cs':'NA',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': 'NA',
    'gcs_epsg': '4326',
    'subset': [61.57, 61.76, -138.36, -137.85],
    'bands': 3,
    'variables': ['Band1', 'Band2', 'Band3', 'NA'],
    'xy_size':[4514, 3477]
    },
    # Query 8
    {
    'q_num':'8',
    'reference_image':'uavsar_query8_reference.tiff',
    'request_url':'Band2/coverage/rangeset?subset=lat(-40.02:-39.9)&subset=lon(-72.4:-71.98)&format=image%2Ftiff&granuleID=',
    'message':'Spatial subset that extends past west boundary of granule bounding box',
    'prod_gid':'G1223713114-ASF',
    'uat_gid':'G1233284356-ASF',
    'sit_gid':'G1233284356-ASF',
    'outfile':'_uavsar_query8.tiff',
    'cs': 'Geographic',
    'proj_cs':'NA',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': 'NA',
    'gcs_epsg': '4326',
    'subset': [-40.02, -39.9, -72.17, -71.98],
    'bands': 1,
    'variables': ['Band2', 'NA', 'NA', 'NA'],
    'xy_size':[3364, 2159]
    },
    #Query 9
    {
    'q_num':'9',
    'reference_image':'uavsar_query9_reference.tiff',
    'request_url':'all/coverage/rangeset?subset=time(%222016-11-17T23%3A27%3A00Z%22%3A%222016-11-17T23%3A28%3A00Z%22)&subset=lat(28.9:29.0)&subset=lon(-89.1:-88.9)&format=image%2Ftiff',
    'message':'Temporal subset should only return 1 granule. Spatial subset and all 3 variables',
    'prod_gid':'',
    'uat_gid':'',
    'sit_gid':'',
    'outfile':'_uavsar_query9.tiff',
    'cs': 'Geographic',
    'proj_cs':'NA',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': 'NA',
    'gcs_epsg': '4326',
    'subset': [28.9, 29.0, -89.1, -88.9],
    'bands': 3,
    'variables': ['Band1', 'Band2', 'Band3', 'NA'],
    'xy_size':[3600, 1800]
    },
    # Query 10
    {
    'q_num':'10',
    'request_url':'Band1/coverage/rangeset?subset=lat(63.7:64.1)&subset=lon(-145.9:-145.7)&format=image%2Fpng&granuleID=',
    'message':'This query specifies png output and the tests verify that the product file is png.',
    'prod_gid':'G1422449017-ASF',
    'uat_gid':'G1233284367-ASF',
    'sit_gid':'G1233284367-ASF',
    'outfile':'_uavsar_query10',
    'cs': 'Geographic',
    'proj_cs':'NA',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': 'NA',
    'gcs_epsg': '4326',
    'subset': [],
    'bands': 1,
    'variables': ['NA', 'NA', 'NA', 'NA'],
    'xy_size':[0, 0],
    'file_type':'png'
    },
    # Query 11
    {
    'q_num':'11',
    'request_url':'Band1/coverage/rangeset?subset=lat(63.7:64.1)&subset=lon(-145.9:-145.7)&format=image%2Fgif&granuleID=',
    'message':'This query specifies gif output and the tests verify that the product file is gif.',
    'prod_gid':'G1422449017-ASF',
    'uat_gid':'G1233284367-ASF',
    'sit_gid':'G1233284367-ASF',
    'outfile':'_uavsar_query11',
    'cs': 'Geographic',
    'proj_cs':'NA',
    'gcs': 'WGS 84',
    'authority': 'EPSG',
    'proj_epsg': 'NA',
    'gcs_epsg': '4326',
    'subset': [],
    'bands': 1,
    'variables': ['NA', 'NA', 'NA', 'NA'],
    'xy_size':[0, 0],
    'file_type':'gif'
    }
    ]
    return uavsar
