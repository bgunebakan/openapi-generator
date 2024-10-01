/**
 * OpenAPI Petstore
 * This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.server.api;

import java.util.Date;
import org.openapitools.server.model.User;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;

import org.eclipse.microprofile.rest.client.RestClientBuilder;

import java.net.URL;
import java.net.MalformedURLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * OpenAPI Petstore Test
 *
 * API tests for UserApi
 */
public class UserApiTest {

    private UserApi client;
    private String baseUrl = "http://localhost:9080";

    @BeforeEach
    public void setup() throws MalformedURLException {
        client = RestClientBuilder.newBuilder()
                        .baseUrl(new URL(baseUrl))
                        .register(ApiException.class)
                        .build(UserApi.class);
    }

    
    /**
     * Create user
     *
     * This can only be done by the logged in user.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createUserTest() {
        // TODO: test validations
        User user = null;
        //api.createUser(user);
        //Assertions.assertNotNull(response);


    }
    
    /**
     * Creates list of users with given input array
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createUsersWithArrayInputTest() {
        // TODO: test validations
        List<User> user = null;
        //api.createUsersWithArrayInput(user);
        //Assertions.assertNotNull(response);


    }
    
    /**
     * Creates list of users with given input array
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void createUsersWithListInputTest() {
        // TODO: test validations
        List<User> user = null;
        //api.createUsersWithListInput(user);
        //Assertions.assertNotNull(response);


    }
    
    /**
     * Delete user
     *
     * This can only be done by the logged in user.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void deleteUserTest() {
        // TODO: test validations
        String username = null;
        //api.deleteUser(username);
        //Assertions.assertNotNull(response);


    }
    
    /**
     * Get user by user name
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getUserByNameTest() {
        // TODO: test validations
        String username = null;
        //Uni<User> response = api.getUserByName(username);
        //Assertions.assertNotNull(response);


    }
    
    /**
     * Logs user into the system
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void loginUserTest() {
        // TODO: test validations
        String username = null;
        String password = null;
        //Uni<String> response = api.loginUser(username, password);
        //Assertions.assertNotNull(response);


    }
    
    /**
     * Logs out current logged in user session
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void logoutUserTest() {
        // TODO: test validations
        //api.logoutUser();
        //Assertions.assertNotNull(response);


    }
    
    /**
     * Updated user
     *
     * This can only be done by the logged in user.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void updateUserTest() {
        // TODO: test validations
        String username = null;
        User user = null;
        //api.updateUser(username, user);
        //Assertions.assertNotNull(response);


    }
    
}
