#  Copyright (C) 2021 Texas Instruments Incorporated - http://www.ti.com/
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions
#  are met:
#
#    Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
#    Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
#
#    Neither the name of Texas Instruments Incorporated nor the names of
#    its contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import sys
import utils
import yaml

GST_ELEMENT_MAP_PATH = "/opt/edgeai-gst-apps-defect-detection/configs/gst_plugins_map.yaml"


def parse_gst_element_map():
    """
    Helper function to load available gst plugins based on env var. SOC
    """

    if not os.path.exists(GST_ELEMENT_MAP_PATH):
        print("[ERROR] %s does not exist." % (GST_ELEMENT_MAP_PATH))
        sys.exit()

    target = os.environ.get("SOC")
    if not target:
        target = "arm"
        print("[WARNING] SOC env var not specified. Defaulting target to arm.")

    with open(GST_ELEMENT_MAP_PATH, "r") as f:
        gst_element_map = yaml.safe_load(f)

    if target not in gst_element_map:
        print("[ERROR] %s is not specified in the %s." % (target, GST_ELEMENT_MAP_PATH))
        sys.exit()

    return gst_element_map[target]

SOC = os.environ.get("SOC")
gst_element_map = parse_gst_element_map()