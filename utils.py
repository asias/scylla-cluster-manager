#!/usr/bin/env python3

import requests

CMD_FILE_PREFIX = '.cmd.scylla'

SCYLLA_DOWNLOAD = 'http://downloads.scylladb.com'

scylla_package_list = {
    'Local ./scylla-package.tar.gz': '',
    'Scylla 4.4.dev': f'{SCYLLA_DOWNLOAD}/relocatable/unstable/master/2020-12-20T00%3A11%3A59Z/scylla-unified-package-4.4.dev.0.20201220.b3e39d81aa8.tar.gz',
    'Scylla 4.3': f'{SCYLLA_DOWNLOAD}/downloads/scylla/relocatable/scylladb-4.3/scylla-unified-package-4.3.0.0.20210110.000585522.tar.gz',
    'Scylla Enterprise 2021.1.dev': f'{SCYLLA_DOWNLOAD}/enterprise/relocatable/unstable/enterprise/2020-12-31T11%3A42%3A35Z/scylla-enterprise-unified-package-2021.1.dev.0.20201231.b47bcd5ff.tar.gz'
}


def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
