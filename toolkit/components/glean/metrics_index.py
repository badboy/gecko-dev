# -*- Mode: python; indent-tabs-mode: nil; tab-width: 40 -*-
# vim: set filetype=python:
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# ATTENTION: If you make changes to this file you will need to file a bug in
# Data Platform and Tools :: General asking for the changes to be reflected
# in the data pipeline. Otherwise bad things will happen to good people:
# any new metrics files' metrics will not get columns in any datasets.

# Metrics that are sent by Gecko and everyone using Gecko.
# Order is lexicographical, enforced by t/c/glean/tests/pytest/test_yaml_indices.py
gecko_metrics = [
    "browser/base/content/metrics.yaml",
    "dom/media/metrics.yaml",
    "dom/metrics.yaml",
    "gfx/metrics.yaml",
    "netwerk/metrics.yaml",
    "netwerk/protocol/http/metrics.yaml",
    "toolkit/components/glean/metrics.yaml",
    "toolkit/components/processtools/metrics.yaml",
]

# Metrics available in Firefox Desktop
# Order is lexicographical, enforced by t/c/glean/tests/pytest/test_yaml_indices.py
firefox_desktop_metrics = [
    "browser/components/metrics.yaml",
    "browser/components/newtab/metrics.yaml",
    "browser/components/search/metrics.yaml",
    "browser/modules/metrics.yaml",
    "toolkit/components/extensions/metrics.yaml",
    "toolkit/components/nimbus/metrics.yaml",
    "toolkit/components/pdfjs/metrics.yaml",
    "toolkit/components/telemetry/metrics.yaml",
    "toolkit/xre/metrics.yaml",
]

# Metrics from the Firefox Desktop Background Update Task
# Order is lexicographical, enforced by t/c/glean/tests/pytest/test_yaml_indices.py
background_update_metrics = [
    "toolkit/mozapps/update/metrics.yaml",
]

# Test metrics
# Order is lexicographical, enforced by t/c/glean/tests/pytest/test_yaml_indices.py
test_metrics = [
    "toolkit/components/glean/tests/test_metrics.yaml",
]

# The list of all Glean metrics.yaml files, relative to the top src dir.
metrics_yamls = (
    gecko_metrics + firefox_desktop_metrics + background_update_metrics + test_metrics
)

# Pings that are sent by Gecko and everyone using Gecko.
# Order is lexicographical, enforced by t/c/glean/tests/pytest/test_yaml_indices.py
gecko_pings = [
    "toolkit/components/telemetry/pings.yaml",
]

# Pings that are sent by Firefox Desktop.
# Order is lexicographical, enforced by t/c/glean/tests/pytest/test_yaml_indices.py
firefox_desktop_pings = [
    "browser/components/newtab/pings.yaml",
    "toolkit/components/glean/pings.yaml",
]

# Pings from the Firefox Desktop Background Update Task
# Order is lexicographical, enforced by t/c/glean/tests/pytest/test_yaml_indices.py
background_update_pings = [
    "toolkit/mozapps/update/pings.yaml",
]

# Test pings
# Order is lexicographical, enforced by t/c/glean/tests/pytest/test_yaml_indices.py
test_pings = [
    "toolkit/components/glean/tests/test_pings.yaml",
]

# The list of all Glean pings.yaml files, relative to the top src dir.
pings_yamls = gecko_pings + firefox_desktop_pings + background_update_pings + test_pings

# The list of tags that are allowed in the above to files, and their
# descriptions. Currently we restrict to a set scraped from bugzilla
# (via `./mach update-glean-tags`)
# Order is lexicographical, enforced by t/c/glean/tests/pytest/test_yaml_indices.py
tags_yamls = [
    "toolkit/components/glean/tags.yaml",
]
