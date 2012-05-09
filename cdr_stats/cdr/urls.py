#
# CDR-Stats License
# http://www.cdr-stats.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2012 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#
from django.conf.urls.defaults import *
from django.conf import settings
from cdr.views import *


urlpatterns = patterns('cdr.views',
    (r'^$', 'index'),
    (r'^cdr_view/$', 'cdr_view'),
    (r'^cdr_export_csv/$', 'cdr_export_to_csv'),
    (r'^cdr_detail/(?P<id>\w+)/(?P<switch_id>\w+)/$', 'cdr_detail'),
    (r'^global_report/$', 'cdr_global_report'),
    (r'^dashboard/$', 'cdr_dashboard'),
    (r'^hourly_report/$', 'cdr_graph_by_hour'),
    (r'^cdr_overview/$', 'cdr_overview'),
    (r'^cdr_concurrent_calls/$', 'cdr_concurrent_calls'),
    (r'^cdr_realtime/$', 'cdr_realtime'),
    (r'^mail_report/$', 'mail_report'),
    (r'^country_report/$', 'cdr_country_report'),
    (r'^country_report_grid/$', 'country_report_grid'),

    (r'^login/$',   'login_view'),
    (r'^logout/$',  'logout_view'),
	(r'^index/$',   'index'),
	(r'^pleaselog/$', 'pleaselog'),

    (r'^map_view/$', 'migration_view'),

    # Password reset for Customer UI
    (r'^password_reset/$', 'cust_password_reset'),
    (r'^password_reset/done/$', 'cust_password_reset_done'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                    'cust_password_reset_confirm'),
    (r'^reset/done/$', 'cust_password_reset_complete'),
)