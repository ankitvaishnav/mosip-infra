server = 'guinea-sandbox.mosip.net'
user = 'berlin'
password = 'mosip'

sub_pkts = ['id', 'evidence', 'optional']

pkt_conf = {
    'id_schema':  '1.0',
    'rid': "10002100740000220200801104237",  # Created and give by server
    'creation_date' : '2021-02-01T10:42:37.000Z', # Generate fresh
    'prereg_id' : '', # Eg. '37029479274360'
    'machine_id': '10006',
    'center_id': '10001',
    'officer_id': 'berlin',
    'date_time' : '2021-02-01T10:42:37.000+05:30', # Create fresh
    'city': 'Kenitra',
    'province': 'Kenitra',
    'zone': 'Ben Mansour',
    'region' : 'Rabat Sale Kenitra'
}

pkt_prefix = pkt_conf['rid']
pkt_dir = 'data/packet1'
template_dir = pkt_dir + '/template'
unenc_dir = pkt_dir + '/unencrypted'
enc_dir = pkt_dir + '/encrypted'


