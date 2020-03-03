[![Build Status](https://travis-ci.org/oasis-roles/jbosseap.svg?branch=master)](https://travis-ci.org/oasis-roles/jbosseap)

Red Hat JBoss EAP
===========

This role will install and configure Red Hat JBoss EAP. Currently only
"standlone" mode is supported. All configuratuon changes are done through
jboss-cli under the hood.

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent (not tested on older)

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `jbosseap_jboss_server_config: standalone` - which config file to use
  (without .xml extension)
* `jbosseap_clean_config: False` - start EAP with clean/initial config and
  apply all changes against it
* `jbosseap_jboss_home` - home dir of EAP installation
* `jbosseap_jboss_config_dir` - path of config dir
* `jbosseap_jboss_user` - OS user
* `jbosseap_jboss_group` - OS group
* `jbosseap_cli_batch_dir` - path to store .cli generated scripts
* `jbosseap_cli_files` - list of all .cli files which we generate (need this
  list when you do jbosseap_clean_config: True)
* `jbosseap_java_opts` - list of java options (JAVA_OPTS)
* `jbosseap_datasource_packages` - list of system packages to install in order
  to enable the datasources (e.g. mysql-connector-java, postgresql-jdbc, etc)

### System Properties, `<system-properties></system-properties>`
```
jbosseap_system_properties:
  - name: prop1
    value: prop1val1
```

### Logging, `<subsystem xmlns="urn:jboss:domain:logging">`
```
jbosseap_logging:
  logger:
    - category: com.foo
      level: DEBUG
  formatter:
    - name: myformatter
      pattern: XXX
  custom_handler:
    - name: myhandler
      class: com.bla
      module: com.aa
      formantter: XXX
      level: XXX
      properties: '("name1" => "val1"),("name2" => "val2")'
```

### Web, `<subsystem xmlns="urn:jboss:domain:web">`
```
jbosseap_web:
  valve:
    - name: myvalve
      module: com.bla
      class: com.bla
      params: '("name1" => "val1"),("name2" => "val2")'
  virtual_server:
    - name: default-host
      enable-welcome-root: 'true'
```

### JDBC drivers
```
jbosseap_jdbc_drivers:
  - file: file1.jar
```

### Datasources, `<subsystem xmlns="urn:jboss:domain:datasources">`
Note that you need to put literal true/false in single quotes when needed
```
jbosseap_datasources:
  - DS:
    name: MyDS
    connection_url: jdbc:mysql://localhost:3306/dbname
    connection_properties:
      - name: prop1
        value: val1
    jndi_name: java:jboss/datasources/MyDS
    driver_name: mysql.jdbc.Driver_5_1
    jta: 'true'
    connectable: 'true'
    use_java_context: 'true'
    spy: 'true'
    use_ccm: 'true'
    statistics_enabled: 'true'
    driver_class: com.mydriver.jdbc.Driver
    datasource_class: com.datasoure.class
    new_connection_sql: select 1
    transaction_isolation: TRANSACTION_XX
    url_delimiter: XXX
    url_selector_strategy_class_name: XXX
    pool:
      min_pool_size: XXX
      max_pool_size: XXX
      prefil: True
      use_strict_min: 'true'
      flush_strategy: XXX
      allow_multiple_users: 'true'
    security:
      user_name: XXX
      password: XXX
      security_domain: XXX
      reauth_plugin_class_name: XXX
      reauth_plugin_properties: XXX
    validation:
      valid_connection_checker_class_name: XXX
      valid_connection_checker_properties: XXX
      check_valid_connection_sql: XXX
      validate_on_match: 'true'
      background_validation: 'false'
      background_validation_millis: XXX
      use_fast_fail: 'true'
      stale_connection_checker_class_name: XXX
      stale_connection_checker_properties: XXX
      exception_sorter_class_name: XXX
      exception_sorter_properties: XXX
    timeout:
      blocking_timeout_millis: XXX
      idle_timeout_minutes: XXX
      set_tx_query_timeout: XXX
      query_timeout: XXX
      use_try_lock: XXX
      allocation_retry: XXX
      allocation_retry_wait_millis: XXX
    statement:
      track_statements: 'true'
      prepared_statement_cache_size: XXX
      share_prepared_statements: 'true'
```


Dependencies
------------

None

Example Playbook
----------------

```
- hosts: jbosseap-servers
  roles:
    - role: jbosseap
      jbosseap_jdbc_drivers:
        - file: mysql-connector-java-5.1.37-bin.jar
        - file: postgresql-9.4.1207.jar
      jbosseap_datasources:
        - borg:
            name: MysqlDS
            connection_url: jdbc:mysql://localhost:3306/borg
            connection_properties:
              - name: autoReconnect
                value: 'true'
              - name: useUnicode
                value: 'true'
              - name: characterEncoding
                value: UTF-8
              - name: maxReconnects
                value: 999999
            jndi_name: java:jboss/datasources/MysqlDS
            driver_name: mysql-connector-java-5.1.37-bin.jar
            driver_class: com.mysql.jdbc.Driver
            use_java_context: 'true'
            transaction_isolation: TRANSACTION_READ_COMMITTED
            pool:
              min_pool_size: 10
              max_pool_size: 100
              prefill: 'true'
            security:
              user_name: borg
              password: ***
            validation:
              validate_on_match: 'true'
              valid_connection_checker_class_name: org.MySQLValidConnectionChecker
              exception_sorter_class_name: org.MySQLExceptionSorter
            statement:
              prepared_statement_cache_size: 32
              share_prepared_statements: 'true'
```

License
-------

BSD

Author Information
------------------

Greg Hellings <ghelling@redhat.com>
