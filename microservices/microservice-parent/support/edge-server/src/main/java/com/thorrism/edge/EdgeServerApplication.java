/*
 * Copyright (c) 2017 HyTrust Inc. All rights reserved.
 */

package com.thorrism.edge;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;

/**
 * @author lcrawford
 */
@SpringBootApplication
@EnableZuulProxy
@EnableDiscoveryClient
public class EdgeServerApplication {

    public static void main(String[] args) {
        new SpringApplicationBuilder(EdgeServerApplication.class)
                .run(args);
    }
}