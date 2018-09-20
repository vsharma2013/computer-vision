#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:24:09 2018

@author: vishal
"""

import imageio


videos = ['z_bus.mp4', 'z_bus-2.mp4', 'z_cars-opp_new.mp4', 'z_cars-opp-3.mp4', 'z_cars-tl.mp4', 'z_ped.mp4']
writer = None

for video in videos:
    reader = imageio.get_reader(video)
    fps = reader.get_meta_data()['fps']
    if not writer:
        writer = imageio.get_writer('zout.mp4', fps = fps)
    try:
        for i, frame in enumerate(reader):
            try:
                print(i)
                writer.append_data(frame)
            except:
                print("*********** Exception in i = " + str(i))
    except:
        print("### exception in frame reader ####")

writer.close()
