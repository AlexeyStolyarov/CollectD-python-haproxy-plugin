#!/usr/bin/py

data_gathered = {}

data_gathered['info'] = [ 
#'Name', 
#'Version', 
#'Release_date', 
#'Nbproc', 
#'Process_num', 
#'Pid', 
#'Uptime', 
#'Uptime_sec', 
#'Memmax_MB', 
#'Ulimit-n', 
#'Maxsock', 
#'Maxconn', 
#'Hard_maxconn', 
#'CurrConns', 
#'CumConns', 
#'CumReq', 
#'MaxSslConns', 
#'CurrSslConns', 
#'CumSslConns', 
#'Maxpipes', 
#'PipesUsed', 
#'PipesFree', 
#'ConnRate', 
#'ConnRateLimit', 
#'MaxConnRate', 
#'SessRate', 
#'SessRateLimit', 
#'MaxSessRate', 
#'SslRate', 
#'SslRateLimit', 
#'MaxSslRate', 
#'SslFrontendKeyRate', 
#'SslFrontendMaxKeyRate', 
#'SslFrontendSessionReuse_pct', 
#'SslBackendKeyRate', 
#'SslBackendMaxKeyRate', 
#'SslCacheLookups', 
#'SslCacheMisses', 
#'CompressBpsIn', 
#'CompressBpsOut', 
#'CompressBpsRateLim', 
#'ZlibMemUsage', 
#'MaxZlibMemUsage', 
#'Tasks', 
#'Run_queue', 
#'Idle_pct', 
#'node', 
#'description'
]


data_gathered['stat'] = [ 
#'pxname',
#'svname',
'qcur',
'scur',
'stot',
'bin',
'bout',
'dreq',
'dresp',
'ereqeconeresp',
]


data_stat_index = {
'pxname':0,
'svname':1,
'qcur':2,
'qmax':3,
'scur':4,
'smax':5,
'slim':6,
'stot':7,
'bin':8,
'bout':9,
'dreq':10,
'dresp':11,
'ereqeconeresp':12,
'wretr':13,
'wredis':14,
'status':15,
'weight':16,
'act':17,
'bckchkfail':18,
'chkdown':19,
'lastchg':20,
'downtime':21,
'qlimit':22,
'pid':23,
'iid':24,
'sid':25,
'throttle':26,
'lbtot':27,
'tracked':28,
'type':29,
'rate':30,
'rate_lim':31,
'rate_max':32,
'check_status':33,
'check_code':34,
'check_duration':35,
'hrsp_1xx':36,
'hrsp_2xx':37,
'hrsp_3xx':38,
'hrsp_4xx':39,
'hrsp_5xx':40,
'hrsp_other':41,
'hanafail':42,
'req_rate':43,
'req_rate_max':44,
'req_tot':45,
'cli_abrt':46,
'srv_abrt':47,
'comp_in':48,
'comp_out':49,
'comp_byp':50,
'comp_rsp':51,
'lastsess':52,
'last_chk':53,
'last_agt':54,
'qtime':55,
'ctime':56,
'rtime':57,
'ttime':58,
'agent_status':59,
'agent_code':60,
'agent_duration':61,
'check_desc':62,
'agent_desc':63,
'check_rise':64,
'check_fall':65,
'check_health':66,
'agent_rise':67,
'agent_fall':68,
'agent_health':69,
'addr':70,
'cookie':71,
'mode':72,
'algo':73,
'conn_rate':74,
'conn_rate_max':75,
'conn_tot':76,
'intercepted':77,
'dcon':78,
'dses':79
}
