from enum import Enum

class Block(str, Enum):
    DATA = "data"
    LOCAL = "local"
    MODULE = "module"
    OUTPUT = "output"
    PROVIDER = "provider"
    RESOURCE = "resource"
    TERRAFORM = "terraform"
    VARIABLE = "variable"

class Provider(str, Enum):
    AWS = "aws"
    NCP = "ncloud"

class NCPResource(str, Enum):
    
    NCLOUD_ACCESS_CONTROL_GROUP = "ncloud_access_control_group"
    NCLOUD_ACCESS_CONTROL_GROUP_RULE = "ncloud_access_control_group_rule"
    NCLOUD_AUTO_SCALING_GROUP = "ncloud_auto_scaling_group"
    NCLOUD_AUTO_SCALING_POLICY = "ncloud_auto_scaling_policy"
    NCLOUD_AUTO_SCALING_SCHEDULE = "ncloud_auto_scaling_schedule"
    NCLOUD_BLOCK_STORAGE = "ncloud_block_storage"
    NCLOUD_BLOCK_STORAGE_SNAPSHOT = "ncloud_block_storage_snapshot"
    NCLOUD_INIT_SCRIPT = "ncloud_init_script"
    NCLOUD_LAUNCH_CONFIGURATION = "ncloud_launch_configuration"
    NCLOUD_LB = "ncloud_lb"
    NCLOUD_LB_LISTENER = "ncloud_lb_listener"
    NCLOUD_LB_TARGET_GROUP = "ncloud_lb_target_group"
    NCLOUD_LB_TARGET_GROUP_ATTACHMENT = "ncloud_lb_target_group_attachment"
    NCLOUD_LOAD_BALANCER = "nclound_load_balancer"
    NCLOUD_LOAD_BALANCER_SSL_CERTIFICATE = "ncloud_load_balancer_ssl_certificate"
    NCLOUD_LOGIN_KEY = "ncloud_login_key"
    NCLOUD_NAS_VOLUME = "ncloud_nas_volume"
    NCLOUD_NAT_GATEWAY = "ncloud_nat_gateway"
    NCLOUD_NETWORK_ACL = "ncloud_network_acl"
    NCLOUD_NETWORK_ACL_DENY_ALLOW_GROUP = "ncloud_network_acl_deny_allow_group"
    NCLOUD_NETWORK_ACL_RULE = "ncloud_network_acl_rule"
    NCLOUD_NETWORK_INTERFACE = "ncloud_network_interface"
    NCLOUD_NKS_CLUSTER = "ncloud_nks_cluster"
    NCLOUD_NKS_NODE_POOL = "ncloud_nks_node_pool"
    NCLOUD_PLACEMENT_GROUP = "ncloud_placement_group"
    NCLOUD_PORT_FORWARDING_RULE = "ncloud_port_forwarding_rule"
    NCLOUD_PUBLIC_IP = "ncloud_public_ip"
    NCLOUD_ROUTE = "ncloud_route"
    NCLOUD_ROUTE_TABLE = "ncloud_route_table"
    NCLOUD_ROUTE_TABLE_ASSOCIATION = "ncloud_route_table_association"
    NCLOUD_SERVER = "ncloud_server"
    NCLOUD_SOURCEBUILD_PROJECT = "ncloud_sourcebuild_project"
    NCLOUD_SOURCECOMMIT_REPOSITORY = "ncloud_sourcecommit_repository"
    NCLOUD_SOURCEDEPLOY_PROJECT = "ncloud_sourcedeploy_project"
    NCLOUD_SOURCEDEPLOY_PROJECT_STAGE = "ncloud_sourcedeploy_project_stage"
    NCLOUD_SOURCEDEPLOY_PROJECT_STAGE_SCENARIO = "ncloud_sourcedeploy_project_stage_scenario"
    NCLOUD_SOURCEPIPELINE_PROJECT = "ncloud_sourcepipeline_project"
    NCLOUD_SUBNET = "ncloud_subnet"
    NCLOUD_VPC = "ncloud_vpc"
    NCLOUD_VPC_PEERING = "ncloud_vpc_peering"


class NCPData(str, Enum):
    NCLOUD_ACCESS_CONTROL_GROUP = "ncloud_access_control_group"
    NCLOUD_ACCESS_CONTROL_GROUPS = "ncloud_access_control_groups"
    NCLOUD_ACCESS_CONTROL_GROUP_RULE = "ncloud_access_control_group_rule"
    NCLOUD_ACCESS_CONTROL_GROUP_RULES = "ncloud_access_control_group_rules"
    NCLOUD_AUTO_SCALING_GROUP = "ncloud_auto_scaling_group"
    NCLOUD_AUTO_SCALING_POLICY = "ncloud_auto_scaling_policy"
    NCLOUD_AUTO_SCALING_SCHEDULE = "ncloud_auto_scaling_schedule"
    NCLOUD_BLOCK_STORAGE = "ncloud_block_storage"
    NCLOUD_BLOCK_STORAGE_SNAPSHOT = "ncloud_block_storage_snapshot"
    NCLOUD_INIT_SCRIPT = "ncloud_init_script"
    NCLOUD_LAUNCH_CONFIGURATION = "ncloud_launch_configuration"
    NCLOUD_LB = "ncloud_lb"
    NCLOUD_LB_LISTENER = "ncloud_lb_listener"
    NCLOUD_LB_TARGET_GROUP = "ncloud_lb_target_group"
    NCLOUD_MEMBER_SERVER_IMAGE = "ncloud_member_server_image"
    NCLOUD_MEMBER_SERVER_IMAGES = "ncloud_member_server_images"
    NCLOUD_NAS_VOLUME = "ncloud_nas_volume"
    NCLOUD_NAS_VOLUMES = "ncloud_nas_volumes"
    NCLOUD_NAT_GATEWAY = "ncloud_nat_gateway"
    NCLOUD_NETWORK_ACL_DENY_ALLOW_GROUPS = "ncloud_network_acl_deny_allow_groups"
    NCLOUD_NETWORK_ACLS = "ncloud_network_acls"
    NCLOUD_NETWORK_INTERFACE = "ncloud_network_interface"
    NCLOUD_NKS_CLUSTER = "ncloud_nks_cluster"
    NCLOUD_NKS_CLUSTERS = "ncloud_nks_clusters"
    NCLOUD_NKS_NODE_POOL = "ncloud_nks_node_pool"
    NCLOUD_NKS_NODE_POOLS = "ncloud_nks_node_pools"
    NCLOUD_NKS_VERSIONS = "ncloud_nks_versions"
    NCLOUD_PLACEMENT_GROUP = "ncloud_placement_group"
    NCLOUD_PORT_FORWARDING_RULE = "ncloud_port_forwarding_rule"
    NCLOUD_PORT_FORWARDING_RULES = "ncloud_port_forwarding_rules"
    NCLOUD_PUBLIC_IP = "ncloud_public_ip"
    NCLOUD_REGIONS = "ncloud_regions"
    NCLOUD_ROOT_PASSWORD = "ncloud_root_password"
    NCLOUD_ROUTE_TABLE = "ncloud_route_table"
    NCLOUD_ROUTE_TABLES = "ncloud_route_tables"
    NCLOUD_SERVER = "ncloud_server"
    NCLOUD_SERVER_IMAGE = "ncloud_server_image"
    NCLOUD_SERVER_IMAGES = "ncloud_server_images"
    NCLOUD_SERVER_PRODUCT = "ncloud_server_product"
    NCLOUD_SERVER_PRODUCTS = "ncloud_server_products"
    NCLOUD_SOURCEBUILD_PROJECT = "ncloud_sourcebuild_project"
    NCLOUD_SOURCEBUILD_PROJECT_COMPUTES = "ncloud_sourcebuild_project_computes"
    NCLOUD_SOURCEBUILD_PROJECT_DOCKER_ENGINES = "ncloud_sourcebuild_project_docker_engines"
    NCLOUD_SOURCEBUILD_PROJECT_OS = "ncloud_sourcebuild_project_os"
    NCLOUD_SOURCEBUILD_PROJECT_OS_RUNTIMES = "ncloud_sourcebuild_project_os_runtimes"
    NCLOUD_SOURCEBUILD_PROJECTS = "ncloud_sourcebuild_projects"
    NCLOUD_SOURCECOMMIT_REPOSITORIES = "ncloud_sourcecommit_repositories"
    NCLOUD_SOURCECOMMIT_REPOSITORY = "ncloud_sourcecommit_repository"
    NCLOUD_SOURCEDEPLOY_PROJECT_STAGE = "ncloud_sourcedeploy_project_stage"
    NCLOUD_SOURCEDEPLOY_PROJECT_STAGE_SCENARIO = "ncloud_sourcedeploy_project_stage_scenario"
    NCLOUD_SOURCEDEPLOY_PROJECT_STAGE_SCENARIOS = "ncloude_sourcedeploy_project_stage_scenarios"
    NCLOUD_SOURCEDEPLOY_PROJECTS = "ncloud_sourcedeploy_projects"
    NCLOUD_SOURCEPIPELINE_PROJECTS = "ncloud_sourcepipeline_projects"
    NCLOUD_SOURCEPIPELINE_PROJECT = "ncloud_sourcepipeline_project"
    NCLOUD_SUBNET = "ncloud_subnet"
    NCLOUD_SUBNETS = "ncloud_subnets"
    NCLOUD_VPC = "ncloud_vpc"
    NCLOUD_VPC_PEERING = "ncloud_vpc_peering"
    NCLOUD_VPCS = "ncloud_vpcs"
    NCLOUD_ZONES = "ncloud_zone"


class AWSResource(str, Enum):
    # ACM
    AWS_ACM_CERTIFICATE = "aws_acm_certificate"
    AWS_ACM_CERTIFICATE_VALIDATION = "aws_acm_certificate_validation"

    # ACM PCA
    AWS_ACMPCA_CERTIFICATE = "aws_acmpca_certificate"
    AWS_ACMPCA_CERTIFICATE_AUTHORITY = "aws_acmpca_certificate_authority"
    AWS_ACMPCA_CERTIFICATE_AUTHORITY_CERTIFICATE = "aws_acmpca_certificate_authority_certificate"
    AWS_ACMPCA_PERMISSION = "aws_acmpca_permission"
    AWS_ACMPCA_POLICY = "aws_acmpca_policy"

    # AMP
    AWS_PROMETHEUS_ALERT_MANAGER_DEFINITION = "aws_prometheus_alert_manager_definition"
    AWS_PROMETHEUS_RULE_GROUP_NAMESPACE = "aws_prometheus_rule_group_namespace"
    AWS_PROMETHEUS_WORKSPACE = "aws_prometheus_workspace"

    # API Gateway
    AWS_API_GATEWAY_ACCOUNT = "aws_api_gateway_account"
    AWS_API_GATEWAY_API_KEY = "aws_api_gateway_api_key"
    AWS_API_GATEWAY_AUTHORIZER = "aws_api_gateway_authorizer"
    AWS_API_GATEWAY_BASE_PATH_MAPPING = "aws_api_gateway_base_path_mapping"
    AWS_API_GATEWAY_CLIENT_CERTIFICATE = "aws_api_gateway_client_certificate"
    AWS_API_GATEWAY_DEPLOYMENT = "aws_api_gateway_deployment"
    AWS_API_GATEWAY_DOCUMENTATION_PART = "aws_api_gateway_documentation_part"
    AWS_API_GATEWAY_DOCUMENTATION_VERSION = "aws_api_gateway_documentation_version"
    AWS_API_GATEWAY_DOMAIN_NAME = "aws_api_gateway_domain_name"
    AWS_API_GATEWAY_GATEWAY_RESPONSE = "aws_api_gateway_gateway_response"
    AWS_API_GATEWAY_INTEGRATION = "aws_api_gateway_integration"
    AWS_API_GATEWAY_INTEGRATION_RESPONSE = "aws_api_gateway_integration_response"
    AWS_API_GATEWAY_METHOD = "aws_api_gateway_method"
    AWS_API_GATEWAY_METHOD_RESPONSE = "aws_api_gateway_method_response"
    AWS_API_GATEWAY_METHOD_SETTINGS = "aws_api_gateway_method_settings"
    AWS_API_GATEWAY_MODEL = "aws_api_gateway_model"
    AWS_API_GATEWAY_REQUEST_VALIDATOR = "aws_api_gateway_request_validator"
    AWS_API_GATEWAY_RESOURCE = "aws_api_gateway_resource"
    AWS_API_GATEWAY_REST_API = "aws_api_gateway_rest_api"
    AWS_API_GATEWAY_REST_API_POLICY = "aws_api_gateway_rest_api_policy"
    AWS_API_GATEWAY_STAGE = "aws_api_gateway_stage"
    AWS_API_GATEWAY_USAGE_PLAN = "aws_api_gateway_usage_plan"
    AWS_API_GATEWAY_USAGE_PLAN_KEY = "aws_api_gateway_usage_plan_key"
    AWS_API_GATEWAY_VPC_LINK = "aws_api_gateway_vpc_link"

    # API Gateway V2
    AWS_APIGATEWAYV2_API = "aws_apigatewayv2_api"
    AWS_APIGATEWAYV2_API_MAPPING = "aws_apigatewayv2_api_mapping"
    AWS_APIGATEWAYV2_AUTHORIZER = "aws_apigatewayv2_authorizer"
    AWS_APIGATEWAYV2_DEPLOYMENT = "aws_apigatewayv2_deployment"
    AWS_APIGATEWAYV2_DOMAIN_NAME = "aws_apigatewayv2_domain_name"
    AWS_APIGATEWAYV2_INTEGRATION = "aws_apigatewayv2_integration"
    AWS_APIGATEWAYV2_INTEGRATION_RESPONSE = "aws_apigatewayv2_integration_response"
    AWS_APIGATEWAYV2_MODEL = "aws_apigatewayv2_model"
    AWS_APIGATEWAYV2_ROUTE = "aws_apigatewayv2_route"
    AWS_APIGATEWAYV2_ROUTE_RESPONSE = "aws_apigatewayv2_route_response"
    AWS_APIGATEWAYV2_STAGE = "aws_apigatewayv2_stage"
    AWS_APIGATEWAYV2_VPC_LINK = "aws_apigatewayv2_vpc_link"

    # Account Management
    AWS_ACCOUNT_ALTERNATE_CONTACT = "aws_account_alternate_contact"

    # Amplify
    AWS_AMPLIFY_APP = "aws_amplify_app"
    AWS_AMPLIFY_BACKEND_ENVIRONMENT = "aws_amplify_backend_environment"
    AWS_AMPLIFY_BRANCH = "aws_amplify_branch"
    AWS_AMPLIFY_DOMAIN_ASSOCIATION = "aws_amplify_domain_association"
    AWS_AMPLIFY_WEBHOOK = "aws_amplify_webhook"

    # App Mesh
    AWS_APPMESH_GATEWAY_ROUTE = "aws_appmesh_gateway_route"
    AWS_APPMESH_MESH = "aws_appmesh_mesh"
    AWS_APPMESH_ROUTE = "aws_appmesh_route"
    AWS_APPMESH_VIRTUAL_GATEWAY = "aws_appmesh_virtual_gateway"
    AWS_APPMESH_VIRTUAL_NODE = "aws_appmesh_virtual_node"
    AWS_APPMESH_VIRTUAL_ROUTER = "aws_appmesh_virtual_router"
    AWS_APPMESH_VIRTUAL_SERVICE = "aws_appmesh_virtual_service"

    # App Runner
    AWS_APPRUNNER_AUTO_SCALING_CONFIGURATION_VERSION = "aws_apprunner_auto_scaling_configuration_version"
    AWS_APPRUNNER_CONNECTION = "aws_apprunner_connection"
    AWS_APPRUNNER_CUSTOM_DOMAIN_ASSOCIATION = "aws_apprunner_custom_domain_association"
    AWS_APPRUNNER_OBSERVABILITY_CONFIGURATION = "aws_apprunner_observability_configuration"
    AWS_APPRUNNER_SERVICE = "aws_apprunner_service"
    AWS_APPRUNNER_VPC_CONNECTOR = "aws_apprunner_vpc_connector"
    AWS_APPRUNNER_VPC_INGRESS_CONNECTION = "aws_apprunner_vpc_ingress_connection"

    # AppConfig
    AWS_APPCONFIG_APPLICATION = "aws_appconfig_application"
    AWS_APPCONFIG_CONFIGURATION_PROFILE = "aws_appconfig_configuration_profile"
    AWS_APPCONFIG_DEPLOYMENT = "aws_appconfig_deployment"
    AWS_APPCONFIG_DEPLOYMENT_STRATEGY = "aws_appconfig_deployment_strategy"
    AWS_APPCONFIG_ENVIRONMENT = "aws_appconfig_environment"
    AWS_APPCONFIG_EXTENSION = "aws_appconfig_extension"
    AWS_APPCONFIG_EXTENSION_ASSOCIATION = "aws_appconfig_extension_association"
    AWS_APPCONFIG_HOSTED_CONFIGURATION_VERSION = "aws_appconfig_hosted_configuration_version"

    # AppFlow
    AWS_APPFLOW_CONNECTOR_PROFILE = "aws_appflow_connector_profile"
    AWS_APPFLOW_FLOW = "aws_appflow_flow"
    AWS_APPINTEGRATIONS_EVENT_INTEGRATION = "aws_appintegrations_event_integration"

    # AppStream 2.0
    AWS_APPSTREAM_DIRECTORY_CONFIG = "aws_appstream_directory_config"
    AWS_APPSTREAM_FLEET = "aws_appstream_fleet"
    AWS_APPSTREAM_FLEET_STACK_ASSOCIATION = "aws_appstream_fleet_stack_association"
    AWS_APPSTREAM_IMAGE_BUILDER = "aws_appstream_image_builder"
    AWS_APPSTREAM_STACK = "aws_appstream_stack"
    AWS_APPSTREAM_USER = "aws_appstream_user"
    AWS_APPSTREAM_USER_STACK_ASSOCIATION = "aws_appstream_user_stack_association"

    # AppSync
    AWS_APPSYNC_API_CACHE = "aws_appsync_api_cache"
    AWS_APPSYNC_API_KEY = "aws_appsync_api_key"
    AWS_APPSYNC_DATASOURCE = "aws_appsync_datasource"
    AWS_APPSYNC_DOMAIN_NAME = "aws_appsync_domain_name"
    AWS_APPSYNC_DOMAIN_NAME_API_ASSOCIATION = "aws_appsync_domain_name_api_association"
    AWS_APPSYNC_FUNCTION = "aws_appsync_function"
    AWS_APPSYNC_GRAPHQL_API = "aws_appsync_graphql_api"
    AWS_APPSYNC_RESOLVER = "aws_appsync_resolver"

    # Application Auto Scaling
    AWS_APPAUTOSCALING_POLICY = "aws_appautoscaling_policy"
    AWS_APPAUTOSCALING_SCHEDULED_ACTION = "aws_appautoscaling_scheduled_action"
    AWS_APPAUTOSCALING_TARGET = "aws_appautoscaling_target"

    # Athena
    AWS_ATHENA_DATA_CATALOG = "aws_athena_data_catalog"
    AWS_ATHENA_DATABASE = "aws_athena_database"
    AWS_ATHENA_NAMED_QUERY = "aws_athena_named_query"
    AWS_ATHENA_WORKGROUP = "aws_athena_workgroup"

    # Auto Scaling
    AWS_AUTOSCALING_ATTACHMENT = "aws_autoscaling_attachment"
    AWS_AUTOSCALING_GROUP = "aws_autoscaling_group"
    AWS_AUTOSCALING_GROUP_TAG = "aws_autoscaling_group_tag"
    AWS_AUTOSCALING_LIFECYCLE_HOOK = "aws_autoscaling_lifecycle_hook"
    AWS_AUTOSCALING_NOTIFICATION = "aws_autoscaling_notification"
    AWS_AUTOSCALING_POLICY = "aws_autoscaling_policy"
    AWS_AUTOSCALING_SCHEDULE = "aws_autoscaling_schedule"
    AWS_LAUNCH_CONFIGURATION = "aws_launch_configuration"
    AWS_AUTOSCALINGPLANS_SCALING_PLAN = "aws_autoscalingplans_scaling_plan"

    # Backup
    AWS_BACKUP_FRAMEWORK = "aws_backup_framework"
    AWS_BACKUP_GLOBAL_SETTINGS = "aws_backup_global_settings"
    AWS_BACKUP_PLAN = "aws_backup_plan"
    AWS_BACKUP_REGION_SETTINGS = "aws_backup_region_settings"
    AWS_BACKUP_REPORT_PLAN = "aws_backup_report_plan"
    AWS_BACKUP_SELECTION = "aws_backup_selection"
    AWS_BACKUP_VAULT = "aws_backup_vault"
    AWS_BACKUP_VAULT_LOCK_CONFIGURATION = "aws_backup_vault_lock_configuration"
    AWS_BACKUP_VAULT_NOTIFICATIONS = "aws_backup_vault_notifications"
    AWS_BACKUP_VAULT_POLICY = "aws_backup_vault_policy"

    # Batch
    AWS_BATCH_COMPUTE_ENVIRONMENT = "aws_batch_compute_environment"
    AWS_BATCH_JOB_DEFINITION = "aws_batch_job_definition"
    AWS_BATCH_JOB_QUEUE = "aws_batch_job_queue"
    AWS_BATCH_SCHEDULING_POLICY = "aws_batch_scheduling_policy"
    AWS_CE_ANOMALY_MONITOR = "aws_ce_anomaly_monitor"
    AWS_CE_ANOMALY_SUBSCRIPTION = "aws_ce_anomaly_subscription"
    AWS_CE_COST_ALLOCATION_TAG = "aws_ce_cost_allocation_tag"
    AWS_CE_COST_CATEGORY = "aws_ce_cost_category"

    # Chime
    AWS_CHIME_VOICE_CONNECTOR = "aws_chime_voice_connector"
    AWS_CHIME_VOICE_CONNECTOR_GROUP = "aws_chime_voice_connector_group"
    AWS_CHIME_VOICE_CONNECTOR_LOGGING = "aws_chime_voice_connector_logging"
    AWS_CHIME_VOICE_CONNECTOR_ORIGINATION = "aws_chime_voice_connector_origination"
    AWS_CHIME_VOICE_CONNECTOR_STREAMING = "aws_chime_voice_connector_streaming"
    AWS_CHIME_VOICE_CONNECTOR_TERMINATION = "aws_chime_voice_connector_termination"
    AWS_CHIME_VOICE_CONNECTOR_TERMINATION_CREDENTIALS = "aws_chime_voice_connector_termination_credentials"
    AWS_CLOUDCONTROLAPI_RESOURCE = "aws_cloudcontrolapi_resource"

    # Cloud Map
    AWS_SERVICE_DISCOVERY_HTTP_NAMESPACE = "aws_service_discovery_http_namespace"
    AWS_SERVICE_DISCOVERY_INSTANCE = "aws_service_discovery_instance"
    AWS_SERVICE_DISCOVERY_PRIVATE_DNS_NAMESPACE = "aws_service_discovery_private_dns_namespace"
    AWS_SERVICE_DISCOVERY_PUBLIC_DNS_NAMESPACE = "aws_service_discovery_public_dns_namespace"
    AWS_SERVICE_DISCOVERY_SERVICE = "aws_service_discovery_service"

    # Cloud9
    AWS_CLOUD9_ENVIRONMENT_EC2 = "aws_cloud9_environment_ec2"
    AWS_CLOUD9_ENVIRONMENT_MEMBERSHIP = "aws_cloud9_environment_membership"

    # CloudFormation
    AWS_CLOUDFORMATION_STACK = "aws_cloudformation_stack"
    AWS_CLOUDFORMATION_STACK_SET = "aws_cloudformation_stack_set"
    AWS_CLOUDFORMATION_STACK_SET_INSTANCE = "aws_cloudformation_stack_set_instance"
    AWS_CLOUDFORMATION_TYPE = "aws_cloudformation_type"

    # CloudFront
    AWS_CLOUDFRONT_CACHE_POLICY = "aws_cloudfront_cache_policy"
    AWS_CLOUDFRONT_DISTRIBUTION = "aws_cloudfront_distribution"
    AWS_CLOUDFRONT_FIELD_LEVEL_ENCRYPTION_CONFIG = "aws_cloudfront_field_level_encryption_config"
    AWS_CLOUDFRONT_FIELD_LEVEL_ENCRYPTION_PROFILE = "aws_cloudfront_field_level_encryption_profile"
    AWS_CLOUDFRONT_FUNCTION = "aws_cloudfront_function"
    AWS_CLOUDFRONT_KEY_GROUP = "aws_cloudfront_key_group"
    AWS_CLOUDFRONT_MONITORING_SUBSCRIPTION = "aws_cloudfront_monitoring_subscription"
    AWS_CLOUDFRONT_ORIGIN_ACCESS_CONTROL = "aws_cloudfront_origin_access_control"
    AWS_CLOUDFRONT_ORIGIN_ACCESS_IDENTITY = "aws_cloudfront_origin_access_identity"
    AWS_CLOUDFRONT_ORIGIN_REQUEST_POLICY = "aws_cloudfront_origin_request_policy"
    AWS_CLOUDFRONT_PUBLIC_KEY = "aws_cloudfront_public_key"
    AWS_CLOUDFRONT_REALTIME_LOG_CONFIG = "aws_cloudfront_realtime_log_config"
    AWS_CLOUDFRONT_RESPONSE_HEADERS_POLICY = "aws_cloudfront_response_headers_policy"

    # CloudHSM
    AWS_CLOUDHSM_V2_CLUSTER = "aws_cloudhsm_v2_cluster"
    AWS_CLOUDHSM_V2_HSM = "aws_cloudhsm_v2_hsm"

    # CloudSearch
    AWS_CLOUDSEARCH_DOMAIN = "aws_cloudsearch_domain"
    AWS_CLOUDSEARCH_DOMAIN_SERVICE_ACCESS_POLICY = "aws_cloudsearch_domain_service_access_policy"

    # CloudTrail
    AWS_CLOUDTRAIL = "aws_cloudtrail"
    AWS_CLOUDTRAIL_EVENT_DATA_STORE = "aws_cloudtrail_event_data_store"

    # CloudWatch
    AWS_CLOUDWATCH_COMPOSITE_ALARM = "aws_cloudwatch_composite_alarm"
    AWS_CLOUDWATCH_DASHBOARD = "aws_cloudwatch_dashboard"
    AWS_CLOUDWATCH_METRIC_ALARM = "aws_cloudwatch_metric_alarm"
    AWS_CLOUDWATCH_METRIC_STREAM = "aws_cloudwatch_metric_stream"

    # CloudWatch Application Insights
    AWS_APPLICATIONINSIGHTS_APPLICATION = "aws_applicationinsights_application"
    AWS_EVIDENTLY_FEATURE = "aws_evidently_feature"
    AWS_EVIDENTLY_PROJECT = "aws_evidently_project"
    AWS_EVIDENTLY_SEGMENT = "aws_evidently_segment"
    AWS_CLOUDWATCH_LOG_DESTINATION = "aws_cloudwatch_log_destination"
    AWS_CLOUDWATCH_LOG_DESTINATION_POLICY = "aws_cloudwatch_log_destination_policy"
    AWS_CLOUDWATCH_LOG_GROUP = "aws_cloudwatch_log_group"
    AWS_CLOUDWATCH_LOG_METRIC_FILTER = "aws_cloudwatch_log_metric_filter"
    AWS_CLOUDWATCH_LOG_RESOURCE_POLICY = "aws_cloudwatch_log_resource_policy"
    AWS_CLOUDWATCH_LOG_STREAM = "aws_cloudwatch_log_stream"
    AWS_CLOUDWATCH_LOG_SUBSCRIPTION_FILTER = "aws_cloudwatch_log_subscription_filter"
    AWS_CLOUDWATCH_QUERY_DEFINITION = "aws_cloudwatch_query_definition"

    # CloudWatch RUM
    AWS_RUM_APP_MONITOR = "aws_rum_app_monitor"

    # CloudWatch Synthetics
    AWS_SYNTHETICS_CANARY = "aws_synthetics_canary"

    # CodeArtifact
    AWS_CODEARTIFACT_DOMAIN = "aws_codeartifact_domain"
    AWS_CODEARTIFACT_DOMAIN_PERMISSIONS_POLICY = "aws_codeartifact_domain_permissions_policy"
    AWS_CODEARTIFACT_REPOSITORY = "aws_codeartifact_repository"
    AWS_CODEARTIFACT_REPOSITORY_PERMISSIONS_POLICY = "aws_codeartifact_repository_permissions_policy"

    # CodeBuild
    AWS_CODEBUILD_PROJECT = "aws_codebuild_project"
    AWS_CODEBUILD_REPORT_GROUP = "aws_codebuild_report_group"
    AWS_CODEBUILD_RESOURCE_POLICY = "aws_codebuild_resource_policy"
    AWS_CODEBUILD_SOURCE_CREDENTIAL = "aws_codebuild_source_credential"
    AWS_CODEBUILD_WEBHOOK = "aws_codebuild_webhook"

    # CodeCommit
    AWS_CODECOMMIT_APPROVAL_RULE_TEMPLATE = "aws_codecommit_approval_rule_template"
    AWS_CODECOMMIT_APPROVAL_RULE_TEMPLATE_ASSOCIATION = "aws_codecommit_approval_rule_template_association"
    AWS_CODECOMMIT_REPOSITORY = "aws_codecommit_repository"
    AWS_CODECOMMIT_TRIGGER = "aws_codecommit_trigger"

    # CodeDeploy
    AWS_CODEDEPLOY_APP = "aws_codedeploy_app"
    AWS_CODEDEPLOY_DEPLOYMENT_CONFIG = "aws_codedeploy_deployment_config"
    AWS_CODEDEPLOY_DEPLOYMENT_GROUP = "aws_codedeploy_deployment_group"

    # CodePipeline
    AWS_CODEPIPELINE = "aws_codepipeline"
    AWS_CODEPIPELINE_CUSTOM_ACTION_TYPE = "aws_codepipeline_custom_action_type"
    AWS_CODEPIPELINE_WEBHOOK = "aws_codepipeline_webhook"
    AWS_CODESTARCONNECTIONS_CONNECTION = "aws_codestarconnections_connection"
    AWS_CODESTARCONNECTIONS_HOST = "aws_codestarconnections_host"

    # CodeStar Notifications
    AWS_CODESTARNOTIFICATIONS_NOTIFICATION_RULE = "aws_codestarnotifications_notification_rule"

    # Cognito IDP (Identity Provider)
    AWS_COGNITO_IDENTITY_PROVIDER = "aws_cognito_identity_provider"
    AWS_COGNITO_RESOURCE_SERVER = "aws_cognito_resource_server"
    AWS_COGNITO_RISK_CONFIGURATION = "aws_cognito_risk_configuration"
    AWS_COGNITO_USER = "aws_cognito_user"
    AWS_COGNITO_USER_GROUP = "aws_cognito_user_group"
    AWS_COGNITO_USER_IN_GROUP = "aws_cognito_user_in_group"
    AWS_COGNITO_USER_POOL = "aws_cognito_user_pool"
    AWS_COGNITO_USER_POOL_CLIENT = "aws_cognito_user_pool_client"
    AWS_COGNITO_USER_POOL_DOMAIN = "aws_cognito_user_pool_domain"
    AWS_COGNITO_USER_POOL_UI_CUSTOMIZATION = "aws_cognito_user_pool_ui_customization"
    AWS_COGNITO_IDENTITY_POOL = "aws_cognito_identity_pool"
    AWS_COGNITO_IDENTITY_POOL_PROVIDER_PRINCIPAL_TAG = "aws_cognito_identity_pool_provider_principal_tag"
    AWS_COGNITO_IDENTITY_POOL_ROLES_ATTACHMENT = "aws_cognito_identity_pool_roles_attachment"

    # Comprehend
    AWS_COMPREHEND_DOCUMENT_CLASSIFIER = "aws_comprehend_document_classifier"
    AWS_COMPREHEND_ENTITY_RECOGNIZER = "aws_comprehend_entity_recognizer"

    # Config
    AWS_CONFIG_AGGREGATE_AUTHORIZATION = "aws_config_aggregate_authorization"
    AWS_CONFIG_CONFIG_RULE = "aws_config_config_rule"
    AWS_CONFIG_CONFIGURATION_AGGREGATOR = "aws_config_configuration_aggregator"
    AWS_CONFIG_CONFIGURATION_RECORDER = "aws_config_configuration_recorder"
    AWS_CONFIG_CONFIGURATION_RECORDER_STATUS = "aws_config_configuration_recorder_status"
    AWS_CONFIG_CONFORMANCE_PACK = "aws_config_conformance_pack"
    AWS_CONFIG_DELIVERY_CHANNEL = "aws_config_delivery_channel"
    AWS_CONFIG_ORGANIZATION_CONFORMANCE_PACK = "aws_config_organization_conformance_pack"
    AWS_CONFIG_ORGANIZATION_CUSTOM_RULE = "aws_config_organization_custom_rule"
    AWS_CONFIG_ORGANIZATION_MANAGED_RULE = "aws_config_organization_managed_rule"
    AWS_CONFIG_REMEDIATION_CONFIGURATION = "aws_config_remediation_configuration"

    # Connect
    AWS_CONNECT_BOT_ASSOCIATION = "aws_connect_bot_association"
    AWS_CONNECT_CONTACT_FLOW = "aws_connect_contact_flow"
    AWS_CONNECT_CONTACT_FLOW_MODULE = "aws_connect_contact_flow_module"
    AWS_CONNECT_HOURS_OF_OPERATION = "aws_connect_hours_of_operation"
    AWS_CONNECT_INSTANCE = "aws_connect_instance"
    AWS_CONNECT_INSTANCE_STORAGE_CONFIG = "aws_connect_instance_storage_config"
    AWS_CONNECT_LAMBDA_FUNCTION_ASSOCIATION = "aws_connect_lambda_function_association"
    AWS_CONNECT_PHONE_NUMBER = "aws_connect_phone_number"
    AWS_CONNECT_QUEUE = "aws_connect_queue"
    AWS_CONNECT_QUICK_CONNECT = "aws_connect_quick_connect"
    AWS_CONNECT_ROUTING_PROFILE = "aws_connect_routing_profile"
    AWS_CONNECT_SECURITY_PROFILE = "aws_connect_security_profile"
    AWS_CONNECT_USER = "aws_connect_user"
    AWS_CONNECT_USER_HIERARCHY_GROUP = "aws_connect_user_hierarchy_group"
    AWS_CONNECT_USER_HIERARCHY_STRUCTURE = "aws_connect_user_hierarchy_structure"
    AWS_CONNECT_VOCABULARY = "aws_connect_vocabulary"

    # Control Tower
    AWS_CONTROLTOWER_CONTROL = "aws_controltower_control"

    # Cost and Usage Report
    AWS_CUR_REPORT_DEFINITION = "aws_cur_report_definition"

    # DLM (Data Lifecycle Manager)
    AWS_DLM_LIFECYCLE_POLICY = "aws_dlm_lifecycle_policy"

    # DMS (Database Migration)
    AWS_DMS_CERTIFICATE = "aws_dms_certificate"
    AWS_DMS_ENDPOINT = "aws_dms_endpoint"
    AWS_DMS_EVENT_SUBSCRIPTION = "aws_dms_event_subscription"
    AWS_DMS_REPLICATION_INSTANCE = "aws_dms_replication_instance"
    AWS_DMS_REPLICATION_SUBNET_GROUP = "aws_dms_replication_subnet_group"
    AWS_DMS_REPLICATION_TASK = "aws_dms_replication_task"

    # DS (Directory Service)
    AWS_DIRECTORY_SERVICE_CONDITIONAL_FORWARDER = "aws_directory_service_conditional_forwarder"
    AWS_DIRECTORY_SERVICE_DIRECTORY = "aws_directory_service_directory"
    AWS_DIRECTORY_SERVICE_LOG_SUBSCRIPTION = "aws_directory_service_log_subscription"
    AWS_DIRECTORY_SERVICE_RADIUS_SETTINGS = "aws_directory_service_radius_settings"
    AWS_DIRECTORY_SERVICE_REGION = "aws_directory_service_region"
    AWS_DIRECTORY_SERVICE_SHARED_DIRECTORY = "aws_directory_service_shared_directory"
    AWS_DIRECTORY_SERVICE_SHARED_DIRECTORY_ACCEPTER = "aws_directory_service_shared_directory_accepter"

    # Data Exchange
    AWS_DATAEXCHANGE_DATA_SET = "aws_dataexchange_data_set"
    AWS_DATAEXCHANGE_REVISION = "aws_dataexchange_revision"

    # Data Pipeline
    AWS_DATAPIPELINE_PIPELINE = "aws_datapipeline_pipeline"
    AWS_DATAPIPELINE_PIPELINE_DEFINITION = "aws_datapipeline_pipeline_definition"

    # DataSync
    AWS_DATASYNC_AGENT = "aws_datasync_agent"
    AWS_DATASYNC_LOCATION_EFS = "aws_datasync_location_efs"
    AWS_DATASYNC_LOCATION_FSX_LUSTRE_FILE_SYSTEM = "aws_datasync_location_fsx_lustre_file_system"
    AWS_DATASYNC_LOCATION_FSX_OPENZFS_FILE_SYSTEM = "aws_datasync_location_fsx_openzfs_file_system"
    AWS_DATASYNC_LOCATION_FSX_WINDOWS_FILE_SYSTEM = "aws_datasync_location_fsx_windows_file_system"
    AWS_DATASYNC_LOCATION_HDFS = "aws_datasync_location_hdfs"
    AWS_DATASYNC_LOCATION_NFS = "aws_datasync_location_nfs"
    AWS_DATASYNC_LOCATION_S3 = "aws_datasync_location_s3"
    AWS_DATASYNC_LOCATION_SMB = "aws_datasync_location_smb"
    AWS_DATASYNC_TASK = "aws_datasync_task"

    # Detective
    AWS_DETECTIVE_GRAPH = "aws_detective_graph"
    AWS_DETECTIVE_INVITATION_ACCEPTER = "aws_detective_invitation_accepter"
    AWS_DETECTIVE_MEMBER = "aws_detective_member"

    # Device Farm
    AWS_DEVICEFARM_DEVICE_POOL = "aws_devicefarm_device_pool"
    AWS_DEVICEFARM_INSTANCE_PROFILE = "aws_devicefarm_instance_profile"
    AWS_DEVICEFARM_NETWORK_PROFILE = "aws_devicefarm_network_profile"
    AWS_DEVICEFARM_PROJECT = "aws_devicefarm_project"
    AWS_DEVICEFARM_TEST_GRID_PROJECT = "aws_devicefarm_test_grid_project"
    AWS_DEVICEFARM_UPLOAD = "aws_devicefarm_upload"

    # Direct Connect
    AWS_DX_BGP_PEER = "aws_dx_bgp_peer"
    AWS_DX_CONNECTION = "aws_dx_connection"
    AWS_DX_CONNECTION_ASSOCIATION = "aws_dx_connection_association"
    AWS_DX_CONNECTION_CONFIRMATION = "aws_dx_connection_confirmation"
    AWS_DX_GATEWAY = "aws_dx_gateway"
    AWS_DX_GATEWAY_ASSOCIATION = "aws_dx_gateway_association"
    AWS_DX_GATEWAY_ASSOCIATION_PROPOSAL = "aws_dx_gateway_association_proposal"
    AWS_DX_HOSTED_CONNECTION = "aws_dx_hosted_connection"
    AWS_DX_HOSTED_PRIVATE_VIRTUAL_INTERFACE = "aws_dx_hosted_private_virtual_interface"
    AWS_DX_HOSTED_PRIVATE_VIRTUAL_INTERFACE_ACCEPTER = "aws_dx_hosted_private_virtual_interface_accepter"
    AWS_DX_HOSTED_PUBLIC_VIRTUAL_INTERFACE = "aws_dx_hosted_public_virtual_interface"
    AWS_DX_HOSTED_PUBLIC_VIRTUAL_INTERFACE_ACCEPTER = "aws_dx_hosted_public_virtual_interface_accepter"
    AWS_DX_HOSTED_TRANSIT_VIRTUAL_INTERFACE = "aws_dx_hosted_transit_virtual_interface"
    AWS_DX_HOSTED_TRANSIT_VIRTUAL_INTERFACE_ACCEPTER = "aws_dx_hosted_transit_virtual_interface_accepter"
    AWS_DX_LAG = "aws_dx_lag"
    AWS_DX_PRIVATE_VIRTUAL_INTERFACE = "aws_dx_private_virtual_interface"
    AWS_DX_PUBLIC_VIRTUAL_INTERFACE = "aws_dx_public_virtual_interface"
    AWS_DX_TRANSIT_VIRTUAL_INTERFACE = "aws_dx_transit_virtual_interface"
    AWS_DOCDB_CLUSTER = "aws_docdb_cluster"
    AWS_DOCDB_CLUSTER_INSTANCE = "aws_docdb_cluster_instance"
    AWS_DOCDB_CLUSTER_PARAMETER_GROUP = "aws_docdb_cluster_parameter_group"
    AWS_DOCDB_CLUSTER_SNAPSHOT = "aws_docdb_cluster_snapshot"
    AWS_DOCDB_EVENT_SUBSCRIPTION = "aws_docdb_event_subscription"
    AWS_DOCDB_GLOBAL_CLUSTER = "aws_docdb_global_cluster"
    AWS_DOCDB_SUBNET_GROUP = "aws_docdb_subnet_group"

    # DynamoDB
    AWS_DYNAMODB_CONTRIBUTOR_INSIGHTS = "aws_dynamodb_contributor_insights"
    AWS_DYNAMODB_GLOBAL_TABLE = "aws_dynamodb_global_table"
    AWS_DYNAMODB_KINESIS_STREAMING_DESTINATION = "aws_dynamodb_kinesis_streaming_destination"
    AWS_DYNAMODB_TABLE = "aws_dynamodb_table"
    AWS_DYNAMODB_TABLE_ITEM = "aws_dynamodb_table_item"
    AWS_DYNAMODB_TABLE_REPLICA = "aws_dynamodb_table_replica"
    AWS_DYNAMODB_TAG = "aws_dynamodb_tag"

    # DynamoDB Accelerator (DAX)
    AWS_DAX_CLUSTER = "aws_dax_cluster"
    AWS_DAX_PARAMETER_GROUP = "aws_dax_parameter_group"
    AWS_DAX_SUBNET_GROUP = "aws_dax_subnet_group"

    # EBS (EC2)
    AWS_EBS_DEFAULT_KMS_KEY = "aws_ebs_default_kms_key"
    AWS_EBS_ENCRYPTION_BY_DEFAULT = "aws_ebs_encryption_by_default"
    AWS_EBS_SNAPSHOT = "aws_ebs_snapshot"
    AWS_EBS_SNAPSHOT_COPY = "aws_ebs_snapshot_copy"
    AWS_EBS_SNAPSHOT_IMPORT = "aws_ebs_snapshot_import"
    AWS_EBS_VOLUME = "aws_ebs_volume"
    AWS_SNAPSHOT_CREATE_VOLUME_PERMISSION = "aws_snapshot_create_volume_permission"
    AWS_VOLUME_ATTACHMENT = "aws_volume_attachment"

    # EC2 (Elastic Compute Cloud)
    AWS_AMI = "aws_ami"
    AWS_AMI_COPY = "aws_ami_copy"
    AWS_AMI_FROM_INSTANCE = "aws_ami_from_instance"
    AWS_AMI_LAUNCH_PERMISSION = "aws_ami_launch_permission"
    AWS_EC2_AVAILABILITY_ZONE_GROUP = "aws_ec2_availability_zone_group"
    AWS_EC2_CAPACITY_RESERVATION = "aws_ec2_capacity_reservation"
    AWS_EC2_FLEET = "aws_ec2_fleet"
    AWS_EC2_HOST = "aws_ec2_host"
    AWS_EC2_SERIAL_CONSOLE_ACCESS = "aws_ec2_serial_console_access"
    AWS_EC2_TAG = "aws_ec2_tag"
    AWS_EIP = "aws_eip"
    AWS_EIP_ASSOCIATION = "aws_eip_association"
    AWS_INSTANCE = "aws_instance"
    AWS_KEY_PAIR = "aws_key_pair"
    AWS_LAUNCH_TEMPLATE = "aws_launch_template"
    AWS_PLACEMENT_GROUP = "aws_placement_group"
    AWS_SPOT_DATAFEED_SUBSCRIPTION = "aws_spot_datafeed_subscription"
    AWS_SPOT_FLEET_REQUEST = "aws_spot_fleet_request"
    AWS_SPOT_INSTANCE_REQUEST = "aws_spot_instance_request"
    AWS_IMAGEBUILDER_COMPONENT = "aws_imagebuilder_component"
    AWS_IMAGEBUILDER_CONTAINER_RECIPE = "aws_imagebuilder_container_recipe"
    AWS_IMAGEBUILDER_DISTRIBUTION_CONFIGURATION = "aws_imagebuilder_distribution_configuration"
    AWS_IMAGEBUILDER_IMAGE = "aws_imagebuilder_image"
    AWS_IMAGEBUILDER_IMAGE_PIPELINE = "aws_imagebuilder_image_pipeline"
    AWS_IMAGEBUILDER_IMAGE_RECIPE = "aws_imagebuilder_image_recipe"
    AWS_IMAGEBUILDER_INFRASTRUCTURE_CONFIGURATION = "aws_imagebuilder_infrastructure_configuration"

    # ECR (Elastic Container Registry)
    AWS_ECR_LIFECYCLE_POLICY = "aws_ecr_lifecycle_policy"
    AWS_ECR_PULL_THROUGH_CACHE_RULE = "aws_ecr_pull_through_cache_rule"
    AWS_ECR_REGISTRY_POLICY = "aws_ecr_registry_policy"
    AWS_ECR_REGISTRY_SCANNING_CONFIGURATION = "aws_ecr_registry_scanning_configuration"
    AWS_ECR_REPLICATION_CONFIGURATION = "aws_ecr_replication_configuration"
    AWS_ECR_REPOSITORY = "aws_ecr_repository"
    AWS_ECR_REPOSITORY_POLICY = "aws_ecr_repository_policy"

    # ECR Public
    AWS_ECRPUBLIC_REPOSITORY = "aws_ecrpublic_repository"
    AWS_ECRPUBLIC_REPOSITORY_POLICY = "aws_ecrpublic_repository_policy"

    # ECS (Elastic Container)
    AWS_ECS_ACCOUNT_SETTING_DEFAULT = "aws_ecs_account_setting_default"
    AWS_ECS_CAPACITY_PROVIDER = "aws_ecs_capacity_provider"
    AWS_ECS_CLUSTER = "aws_ecs_cluster"
    AWS_ECS_CLUSTER_CAPACITY_PROVIDERS = "aws_ecs_cluster_capacity_providers"
    AWS_ECS_SERVICE = "aws_ecs_service"
    AWS_ECS_TAG = "aws_ecs_tag"
    AWS_ECS_TASK_DEFINITION = "aws_ecs_task_definition"
    AWS_ECS_TASK_SET = "aws_ecs_task_set"

    # EFS (Elastic File System)
    AWS_EFS_ACCESS_POINT = "aws_efs_access_point"
    AWS_EFS_BACKUP_POLICY = "aws_efs_backup_policy"
    AWS_EFS_FILE_SYSTEM = "aws_efs_file_system"
    AWS_EFS_FILE_SYSTEM_POLICY = "aws_efs_file_system_policy"
    AWS_EFS_MOUNT_TARGET = "aws_efs_mount_target"
    AWS_EFS_REPLICATION_CONFIGURATION = "aws_efs_replication_configuration"

    # EKS (Elastic Kubernetes)
    AWS_EKS_ADDON = "aws_eks_addon"
    AWS_EKS_CLUSTER = "aws_eks_cluster"
    AWS_EKS_FARGATE_PROFILE = "aws_eks_fargate_profile"
    AWS_EKS_IDENTITY_PROVIDER_CONFIG = "aws_eks_identity_provider_config"
    AWS_EKS_NODE_GROUP = "aws_eks_node_group"

    # ELB (Elastic Load Balancing)
    AWS_LB = "aws_lb"
    AWS_LB_LISTENER = "aws_lb_listener"
    AWS_LB_LISTENER_CERTIFICATE = "aws_lb_listener_certificate"
    AWS_LB_LISTENER_RULE = "aws_lb_listener_rule"
    AWS_LB_TARGET_GROUP = "aws_lb_target_group"
    AWS_LB_TARGET_GROUP_ATTACHMENT = "aws_lb_target_group_attachment"

    # ELB Classic
    AWS_APP_COOKIE_STICKINESS_POLICY = "aws_app_cookie_stickiness_policy"
    AWS_ELB = "aws_elb"
    AWS_ELB_ATTACHMENT = "aws_elb_attachment"
    AWS_LB_COOKIE_STICKINESS_POLICY = "aws_lb_cookie_stickiness_policy"
    AWS_LB_SSL_NEGOTIATION_POLICY = "aws_lb_ssl_negotiation_policy"
    AWS_LOAD_BALANCER_BACKEND_SERVER_POLICY = "aws_load_balancer_backend_server_policy"
    AWS_LOAD_BALANCER_LISTENER_POLICY = "aws_load_balancer_listener_policy"
    AWS_LOAD_BALANCER_POLICY = "aws_load_balancer_policy"
    AWS_PROXY_PROTOCOL_POLICY = "aws_proxy_protocol_policy"

    # EMR
    AWS_EMR_CLUSTER = "aws_emr_cluster"
    AWS_EMR_INSTANCE_FLEET = "aws_emr_instance_fleet"
    AWS_EMR_INSTANCE_GROUP = "aws_emr_instance_group"
    AWS_EMR_MANAGED_SCALING_POLICY = "aws_emr_managed_scaling_policy"
    AWS_EMR_SECURITY_CONFIGURATION = "aws_emr_security_configuration"
    AWS_EMR_STUDIO = "aws_emr_studio"
    AWS_EMR_STUDIO_SESSION_MAPPING = "aws_emr_studio_session_mapping"

    # EMR Containers
    AWS_EMRCONTAINERS_VIRTUAL_CLUSTER = "aws_emrcontainers_virtual_cluster"

    # EMR Serverless
    AWS_EMRSERVERLESS_APPLICATION = "aws_emrserverless_application"

    # ElastiCache
    AWS_ELASTICACHE_CLUSTER = "aws_elasticache_cluster"
    AWS_ELASTICACHE_GLOBAL_REPLICATION_GROUP = "aws_elasticache_global_replication_group"
    AWS_ELASTICACHE_PARAMETER_GROUP = "aws_elasticache_parameter_group"
    AWS_ELASTICACHE_REPLICATION_GROUP = "aws_elasticache_replication_group"
    AWS_ELASTICACHE_SECURITY_GROUP = "aws_elasticache_security_group"
    AWS_ELASTICACHE_SUBNET_GROUP = "aws_elasticache_subnet_group"
    AWS_ELASTICACHE_USER = "aws_elasticache_user"
    AWS_ELASTICACHE_USER_GROUP = "aws_elasticache_user_group"
    AWS_ELASTICACHE_USER_GROUP_ASSOCIATION = "aws_elasticache_user_group_association"
    AWS_ELASTIC_BEANSTALK_APPLICATION = "aws_elastic_beanstalk_application"
    AWS_ELASTIC_BEANSTALK_APPLICATION_VERSION = "aws_elastic_beanstalk_application_version"
    AWS_ELASTIC_BEANSTALK_CONFIGURATION_TEMPLATE = "aws_elastic_beanstalk_configuration_template"
    AWS_ELASTIC_BEANSTALK_ENVIRONMENT = "aws_elastic_beanstalk_environment"
    AWS_ELASTICTRANSCODER_PIPELINE = "aws_elastictranscoder_pipeline"
    AWS_ELASTICTRANSCODER_PRESET = "aws_elastictranscoder_preset"

    # Elasticsearch
    AWS_ELASTICSEARCH_DOMAIN = "aws_elasticsearch_domain"
    AWS_ELASTICSEARCH_DOMAIN_POLICY = "aws_elasticsearch_domain_policy"
    AWS_ELASTICSEARCH_DOMAIN_SAML_OPTIONS = "aws_elasticsearch_domain_saml_options"

    # Elemental MediaConvert
    AWS_MEDIA_CONVERT_QUEUE = "aws_media_convert_queue"
    AWS_MEDIALIVE_CHANNEL = "aws_medialive_channel"
    AWS_MEDIALIVE_INPUT = "aws_medialive_input"
    AWS_MEDIALIVE_INPUT_SECURITY_GROUP = "aws_medialive_input_security_group"
    AWS_MEDIALIVE_MULTIPLEX = "aws_medialive_multiplex"
    AWS_MEDIALIVE_MULTIPLEX_PROGRAM = "aws_medialive_multiplex_program"

    # Elemental MediaPackage
    AWS_MEDIA_PACKAGE_CHANNEL = "aws_media_package_channel"
    AWS_MEDIA_STORE_CONTAINER = "aws_media_store_container"
    AWS_MEDIA_STORE_CONTAINER_POLICY = "aws_media_store_container_policy"

    # EventBridge
    AWS_CLOUDWATCH_EVENT_API_DESTINATION = "aws_cloudwatch_event_api_destination"
    AWS_CLOUDWATCH_EVENT_ARCHIVE = "aws_cloudwatch_event_archive"
    AWS_CLOUDWATCH_EVENT_BUS = "aws_cloudwatch_event_bus"
    AWS_CLOUDWATCH_EVENT_BUS_POLICY = "aws_cloudwatch_event_bus_policy"
    AWS_CLOUDWATCH_EVENT_CONNECTION = "aws_cloudwatch_event_connection"
    AWS_CLOUDWATCH_EVENT_PERMISSION = "aws_cloudwatch_event_permission"
    AWS_CLOUDWATCH_EVENT_RULE = "aws_cloudwatch_event_rule"
    AWS_CLOUDWATCH_EVENT_TARGET = "aws_cloudwatch_event_target"

    # EventBridge Scheduler
    AWS_SCHEDULER_SCHEDULE_GROUP = "aws_scheduler_schedule_group"
    AWS_SCHEMAS_DISCOVERER = "aws_schemas_discoverer"
    AWS_SCHEMAS_REGISTRY = "aws_schemas_registry"
    AWS_SCHEMAS_REGISTRY_POLICY = "aws_schemas_registry_policy"
    AWS_SCHEMAS_SCHEMA = "aws_schemas_schema"

    # FIS (Fault Injection Simulator)
    AWS_FIS_EXPERIMENT_TEMPLATE = "aws_fis_experiment_template"

    # FMS (Firewall Manager)
    AWS_FMS_ADMIN_ACCOUNT = "aws_fms_admin_account"
    AWS_FMS_POLICY = "aws_fms_policy"

    # FSx
    AWS_FSX_BACKUP = "aws_fsx_backup"
    AWS_FSX_DATA_REPOSITORY_ASSOCIATION = "aws_fsx_data_repository_association"
    AWS_FSX_FILE_CACHE = "aws_fsx_file_cache"
    AWS_FSX_LUSTRE_FILE_SYSTEM = "aws_fsx_lustre_file_system"
    AWS_FSX_ONTAP_FILE_SYSTEM = "aws_fsx_ontap_file_system"
    AWS_FSX_ONTAP_STORAGE_VIRTUAL_MACHINE = "aws_fsx_ontap_storage_virtual_machine"
    AWS_FSX_ONTAP_VOLUME = "aws_fsx_ontap_volume"
    AWS_FSX_OPENZFS_FILE_SYSTEM = "aws_fsx_openzfs_file_system"
    AWS_FSX_OPENZFS_SNAPSHOT = "aws_fsx_openzfs_snapshot"
    AWS_FSX_OPENZFS_VOLUME = "aws_fsx_openzfs_volume"
    AWS_FSX_WINDOWS_FILE_SYSTEM = "aws_fsx_windows_file_system"

    # GameLift
    AWS_GAMELIFT_ALIAS = "aws_gamelift_alias"
    AWS_GAMELIFT_BUILD = "aws_gamelift_build"
    AWS_GAMELIFT_FLEET = "aws_gamelift_fleet"
    AWS_GAMELIFT_GAME_SERVER_GROUP = "aws_gamelift_game_server_group"
    AWS_GAMELIFT_GAME_SESSION_QUEUE = "aws_gamelift_game_session_queue"
    AWS_GAMELIFT_SCRIPT = "aws_gamelift_script"
    AWS_GLOBALACCELERATOR_ACCELERATOR = "aws_globalaccelerator_accelerator"
    AWS_GLOBALACCELERATOR_ENDPOINT_GROUP = "aws_globalaccelerator_endpoint_group"
    AWS_GLOBALACCELERATOR_LISTENER = "aws_globalaccelerator_listener"

    # Glue
    AWS_GLUE_CATALOG_DATABASE = "aws_glue_catalog_database"
    AWS_GLUE_CATALOG_TABLE = "aws_glue_catalog_table"
    AWS_GLUE_CLASSIFIER = "aws_glue_classifier"
    AWS_GLUE_CONNECTION = "aws_glue_connection"
    AWS_GLUE_CRAWLER = "aws_glue_crawler"
    AWS_GLUE_DATA_CATALOG_ENCRYPTION_SETTINGS = "aws_glue_data_catalog_encryption_settings"
    AWS_GLUE_DEV_ENDPOINT = "aws_glue_dev_endpoint"
    AWS_GLUE_JOB = "aws_glue_job"
    AWS_GLUE_ML_TRANSFORM = "aws_glue_ml_transform"
    AWS_GLUE_PARTITION = "aws_glue_partition"
    AWS_GLUE_PARTITION_INDEX = "aws_glue_partition_index"
    AWS_GLUE_REGISTRY = "aws_glue_registry"
    AWS_GLUE_RESOURCE_POLICY = "aws_glue_resource_policy"
    AWS_GLUE_SCHEMA = "aws_glue_schema"
    AWS_GLUE_SECURITY_CONFIGURATION = "aws_glue_security_configuration"
    AWS_GLUE_TRIGGER = "aws_glue_trigger"
    AWS_GLUE_USER_DEFINED_FUNCTION = "aws_glue_user_defined_function"
    AWS_GLUE_WORKFLOW = "aws_glue_workflow"

    # GuardDuty
    AWS_GUARDDUTY_DETECTOR = "aws_guardduty_detector"
    AWS_GUARDDUTY_FILTER = "aws_guardduty_filter"
    AWS_GUARDDUTY_INVITE_ACCEPTER = "aws_guardduty_invite_accepter"
    AWS_GUARDDUTY_IPSET = "aws_guardduty_ipset"
    AWS_GUARDDUTY_MEMBER = "aws_guardduty_member"
    AWS_GUARDDUTY_ORGANIZATION_ADMIN_ACCOUNT = "aws_guardduty_organization_admin_account"
    AWS_GUARDDUTY_ORGANIZATION_CONFIGURATION = "aws_guardduty_organization_configuration"
    AWS_GUARDDUTY_PUBLISHING_DESTINATION = "aws_guardduty_publishing_destination"
    AWS_GUARDDUTY_THREATINTELSET = "aws_guardduty_threatintelset"

    # IAM (Identity &amp; Access Management)
    AWS_IAM_ACCESS_KEY = "aws_iam_access_key"
    AWS_IAM_ACCOUNT_ALIAS = "aws_iam_account_alias"
    AWS_IAM_ACCOUNT_PASSWORD_POLICY = "aws_iam_account_password_policy"
    AWS_IAM_GROUP = "aws_iam_group"
    AWS_IAM_GROUP_MEMBERSHIP = "aws_iam_group_membership"
    AWS_IAM_GROUP_POLICY = "aws_iam_group_policy"
    AWS_IAM_GROUP_POLICY_ATTACHMENT = "aws_iam_group_policy_attachment"
    AWS_IAM_INSTANCE_PROFILE = "aws_iam_instance_profile"
    AWS_IAM_OPENID_CONNECT_PROVIDER = "aws_iam_openid_connect_provider"
    AWS_IAM_POLICY = "aws_iam_policy"
    AWS_IAM_POLICY_ATTACHMENT = "aws_iam_policy_attachment"
    AWS_IAM_ROLE = "aws_iam_role"
    AWS_IAM_ROLE_POLICY = "aws_iam_role_policy"
    AWS_IAM_ROLE_POLICY_ATTACHMENT = "aws_iam_role_policy_attachment"
    AWS_IAM_SAML_PROVIDER = "aws_iam_saml_provider"
    AWS_IAM_SERVER_CERTIFICATE = "aws_iam_server_certificate"
    AWS_IAM_SERVICE_LINKED_ROLE = "aws_iam_service_linked_role"
    AWS_IAM_SERVICE_SPECIFIC_CREDENTIAL = "aws_iam_service_specific_credential"
    AWS_IAM_SIGNING_CERTIFICATE = "aws_iam_signing_certificate"
    AWS_IAM_USER = "aws_iam_user"
    AWS_IAM_USER_GROUP_MEMBERSHIP = "aws_iam_user_group_membership"
    AWS_IAM_USER_LOGIN_PROFILE = "aws_iam_user_login_profile"
    AWS_IAM_USER_POLICY = "aws_iam_user_policy"
    AWS_IAM_USER_POLICY_ATTACHMENT = "aws_iam_user_policy_attachment"
    AWS_IAM_USER_SSH_KEY = "aws_iam_user_ssh_key"
    AWS_IAM_VIRTUAL_MFA_DEVICE = "aws_iam_virtual_mfa_device"
    AWS_ACCESSANALYZER_ANALYZER = "aws_accessanalyzer_analyzer"
    AWS_ACCESSANALYZER_ARCHIVE_RULE = "aws_accessanalyzer_archive_rule"

    # IVS (Interactive Video)
    AWS_IVS_CHANNEL = "aws_ivs_channel"
    AWS_IVS_PLAYBACK_KEY_PAIR = "aws_ivs_playback_key_pair"
    AWS_IVS_RECORDING_CONFIGURATION = "aws_ivs_recording_configuration"

    # Inspector
    AWS_INSPECTOR_ASSESSMENT_TARGET = "aws_inspector_assessment_target"
    AWS_INSPECTOR_ASSESSMENT_TEMPLATE = "aws_inspector_assessment_template"
    AWS_INSPECTOR_RESOURCE_GROUP = "aws_inspector_resource_group"

    # Inspector V2
    AWS_INSPECTOR2_DELEGATED_ADMIN_ACCOUNT = "aws_inspector2_delegated_admin_account"
    AWS_INSPECTOR2_ENABLER = "aws_inspector2_enabler"
    AWS_INSPECTOR2_ORGANIZATION_CONFIGURATION = "aws_inspector2_organization_configuration"

    # IoT Core
    AWS_IOT_AUTHORIZER = "aws_iot_authorizer"
    AWS_IOT_CERTIFICATE = "aws_iot_certificate"
    AWS_IOT_INDEXING_CONFIGURATION = "aws_iot_indexing_configuration"
    AWS_IOT_LOGGING_OPTIONS = "aws_iot_logging_options"
    AWS_IOT_POLICY = "aws_iot_policy"
    AWS_IOT_POLICY_ATTACHMENT = "aws_iot_policy_attachment"
    AWS_IOT_PROVISIONING_TEMPLATE = "aws_iot_provisioning_template"
    AWS_IOT_ROLE_ALIAS = "aws_iot_role_alias"
    AWS_IOT_THING = "aws_iot_thing"
    AWS_IOT_THING_GROUP = "aws_iot_thing_group"
    AWS_IOT_THING_GROUP_MEMBERSHIP = "aws_iot_thing_group_membership"
    AWS_IOT_THING_PRINCIPAL_ATTACHMENT = "aws_iot_thing_principal_attachment"
    AWS_IOT_THING_TYPE = "aws_iot_thing_type"
    AWS_IOT_TOPIC_RULE = "aws_iot_topic_rule"
    AWS_IOT_TOPIC_RULE_DESTINATION = "aws_iot_topic_rule_destination"
    AWS_KMS_ALIAS = "aws_kms_alias"
    AWS_KMS_CIPHERTEXT = "aws_kms_ciphertext"
    AWS_KMS_CUSTOM_KEY_STORE = "aws_kms_custom_key_store"
    AWS_KMS_EXTERNAL_KEY = "aws_kms_external_key"
    AWS_KMS_GRANT = "aws_kms_grant"
    AWS_KMS_KEY = "aws_kms_key"
    AWS_KMS_REPLICA_EXTERNAL_KEY = "aws_kms_replica_external_key"
    AWS_KMS_REPLICA_KEY = "aws_kms_replica_key"

    # Kendra
    AWS_KENDRA_DATA_SOURCE = "aws_kendra_data_source"
    AWS_KENDRA_EXPERIENCE = "aws_kendra_experience"
    AWS_KENDRA_FAQ = "aws_kendra_faq"
    AWS_KENDRA_INDEX = "aws_kendra_index"
    AWS_KENDRA_QUERY_SUGGESTIONS_BLOCK_LIST = "aws_kendra_query_suggestions_block_list"
    AWS_KENDRA_THESAURUS = "aws_kendra_thesaurus"

    # Keyspaces (for Apache Cassandra)
    AWS_KEYSPACES_KEYSPACE = "aws_keyspaces_keyspace"
    AWS_KEYSPACES_TABLE = "aws_keyspaces_table"

    # Kinesis
    AWS_KINESIS_STREAM = "aws_kinesis_stream"
    AWS_KINESIS_STREAM_CONSUMER = "aws_kinesis_stream_consumer"
    AWS_KINESIS_ANALYTICS_APPLICATION = "aws_kinesis_analytics_application"
    AWS_KINESISANALYTICSV2_APPLICATION = "aws_kinesisanalyticsv2_application"
    AWS_KINESISANALYTICSV2_APPLICATION_SNAPSHOT = "aws_kinesisanalyticsv2_application_snapshot"
    AWS_KINESIS_FIREHOSE_DELIVERY_STREAM = "aws_kinesis_firehose_delivery_stream"

    # Kinesis Video
    AWS_KINESIS_VIDEO_STREAM = "aws_kinesis_video_stream"

    # Lake Formation
    AWS_LAKEFORMATION_DATA_LAKE_SETTINGS = "aws_lakeformation_data_lake_settings"
    AWS_LAKEFORMATION_LF_TAG = "aws_lakeformation_lf_tag"
    AWS_LAKEFORMATION_PERMISSIONS = "aws_lakeformation_permissions"
    AWS_LAKEFORMATION_RESOURCE = "aws_lakeformation_resource"
    AWS_LAKEFORMATION_RESOURCE_LF_TAGS = "aws_lakeformation_resource_lf_tags"

    # Lambda
    AWS_LAMBDA_ALIAS = "aws_lambda_alias"
    AWS_LAMBDA_CODE_SIGNING_CONFIG = "aws_lambda_code_signing_config"
    AWS_LAMBDA_EVENT_SOURCE_MAPPING = "aws_lambda_event_source_mapping"
    AWS_LAMBDA_FUNCTION = "aws_lambda_function"
    AWS_LAMBDA_FUNCTION_EVENT_INVOKE_CONFIG = "aws_lambda_function_event_invoke_config"
    AWS_LAMBDA_FUNCTION_URL = "aws_lambda_function_url"
    AWS_LAMBDA_INVOCATION = "aws_lambda_invocation"
    AWS_LAMBDA_LAYER_VERSION = "aws_lambda_layer_version"
    AWS_LAMBDA_LAYER_VERSION_PERMISSION = "aws_lambda_layer_version_permission"
    AWS_LAMBDA_PERMISSION = "aws_lambda_permission"
    AWS_LAMBDA_PROVISIONED_CONCURRENCY_CONFIG = "aws_lambda_provisioned_concurrency_config"
    AWS_LEX_BOT = "aws_lex_bot"
    AWS_LEX_BOT_ALIAS = "aws_lex_bot_alias"
    AWS_LEX_INTENT = "aws_lex_intent"
    AWS_LEX_SLOT_TYPE = "aws_lex_slot_type"
    AWS_LICENSEMANAGER_ASSOCIATION = "aws_licensemanager_association"
    AWS_LICENSEMANAGER_LICENSE_CONFIGURATION = "aws_licensemanager_license_configuration"

    # Lightsail
    AWS_LIGHTSAIL_CERTIFICATE = "aws_lightsail_certificate"
    AWS_LIGHTSAIL_CONTAINER_SERVICE = "aws_lightsail_container_service"
    AWS_LIGHTSAIL_CONTAINER_SERVICE_DEPLOYMENT_VERSION = "aws_lightsail_container_service_deployment_version"
    AWS_LIGHTSAIL_DATABASE = "aws_lightsail_database"
    AWS_LIGHTSAIL_DISK = "aws_lightsail_disk"
    AWS_LIGHTSAIL_DISK_ATTACHMENT = "aws_lightsail_disk_attachment"
    AWS_LIGHTSAIL_DOMAIN = "aws_lightsail_domain"
    AWS_LIGHTSAIL_DOMAIN_ENTRY = "aws_lightsail_domain_entry"
    AWS_LIGHTSAIL_INSTANCE = "aws_lightsail_instance"
    AWS_LIGHTSAIL_INSTANCE_PUBLIC_PORTS = "aws_lightsail_instance_public_ports"
    AWS_LIGHTSAIL_KEY_PAIR = "aws_lightsail_key_pair"
    AWS_LIGHTSAIL_LB = "aws_lightsail_lb"
    AWS_LIGHTSAIL_LB_ATTACHMENT = "aws_lightsail_lb_attachment"
    AWS_LIGHTSAIL_LB_CERTIFICATE = "aws_lightsail_lb_certificate"
    AWS_LIGHTSAIL_LB_CERTIFICATE_ATTACHMENT = "aws_lightsail_lb_certificate_attachment"
    AWS_LIGHTSAIL_LB_HTTPS_REDIRECTION_POLICY = "aws_lightsail_lb_https_redirection_policy"
    AWS_LIGHTSAIL_LB_STICKINESS_POLICY = "aws_lightsail_lb_stickiness_policy"
    AWS_LIGHTSAIL_STATIC_IP = "aws_lightsail_static_ip"
    AWS_LIGHTSAIL_STATIC_IP_ATTACHMENT = "aws_lightsail_static_ip_attachment"

    # Location
    AWS_LOCATION_GEOFENCE_COLLECTION = "aws_location_geofence_collection"
    AWS_LOCATION_MAP = "aws_location_map"
    AWS_LOCATION_PLACE_INDEX = "aws_location_place_index"
    AWS_LOCATION_ROUTE_CALCULATOR = "aws_location_route_calculator"
    AWS_LOCATION_TRACKER = "aws_location_tracker"
    AWS_LOCATION_TRACKER_ASSOCIATION = "aws_location_tracker_association"

    # MQ
    AWS_MQ_BROKER = "aws_mq_broker"
    AWS_MQ_CONFIGURATION = "aws_mq_configuration"

    # MWAA (Managed Workflows for Apache Airflow)
    AWS_MWAA_ENVIRONMENT = "aws_mwaa_environment"

    # Macie
    AWS_MACIE2_ACCOUNT = "aws_macie2_account"
    AWS_MACIE2_CLASSIFICATION_EXPORT_CONFIGURATION = "aws_macie2_classification_export_configuration"
    AWS_MACIE2_CLASSIFICATION_JOB = "aws_macie2_classification_job"
    AWS_MACIE2_CUSTOM_DATA_IDENTIFIER = "aws_macie2_custom_data_identifier"
    AWS_MACIE2_FINDINGS_FILTER = "aws_macie2_findings_filter"
    AWS_MACIE2_INVITATION_ACCEPTER = "aws_macie2_invitation_accepter"
    AWS_MACIE2_MEMBER = "aws_macie2_member"
    AWS_MACIE2_ORGANIZATION_ADMIN_ACCOUNT = "aws_macie2_organization_admin_account"

    # Macie Classic
    AWS_MACIE_MEMBER_ACCOUNT_ASSOCIATION = "aws_macie_member_account_association"
    AWS_MACIE_S3_BUCKET_ASSOCIATION = "aws_macie_s3_bucket_association"
    AWS_GRAFANA_LICENSE_ASSOCIATION = "aws_grafana_license_association"
    AWS_GRAFANA_ROLE_ASSOCIATION = "aws_grafana_role_association"
    AWS_GRAFANA_WORKSPACE = "aws_grafana_workspace"
    AWS_GRAFANA_WORKSPACE_API_KEY = "aws_grafana_workspace_api_key"
    AWS_GRAFANA_WORKSPACE_SAML_CONFIGURATION = "aws_grafana_workspace_saml_configuration"

    # Managed Streaming for Kafka
    AWS_MSK_CLUSTER = "aws_msk_cluster"
    AWS_MSK_CONFIGURATION = "aws_msk_configuration"
    AWS_MSK_SCRAM_SECRET_ASSOCIATION = "aws_msk_scram_secret_association"
    AWS_MSK_SERVERLESS_CLUSTER = "aws_msk_serverless_cluster"

    # Managed Streaming for Kafka Connect
    AWS_MSKCONNECT_CONNECTOR = "aws_mskconnect_connector"
    AWS_MSKCONNECT_CUSTOM_PLUGIN = "aws_mskconnect_custom_plugin"
    AWS_MSKCONNECT_WORKER_CONFIGURATION = "aws_mskconnect_worker_configuration"
    AWS_MEMORYDB_ACL = "aws_memorydb_acl"
    AWS_MEMORYDB_CLUSTER = "aws_memorydb_cluster"
    AWS_MEMORYDB_PARAMETER_GROUP = "aws_memorydb_parameter_group"
    AWS_MEMORYDB_SNAPSHOT = "aws_memorydb_snapshot"
    AWS_MEMORYDB_SUBNET_GROUP = "aws_memorydb_subnet_group"
    AWS_MEMORYDB_USER = "aws_memorydb_user"

    # Neptune
    AWS_NEPTUNE_CLUSTER = "aws_neptune_cluster"
    AWS_NEPTUNE_CLUSTER_ENDPOINT = "aws_neptune_cluster_endpoint"
    AWS_NEPTUNE_CLUSTER_INSTANCE = "aws_neptune_cluster_instance"
    AWS_NEPTUNE_CLUSTER_PARAMETER_GROUP = "aws_neptune_cluster_parameter_group"
    AWS_NEPTUNE_CLUSTER_SNAPSHOT = "aws_neptune_cluster_snapshot"
    AWS_NEPTUNE_EVENT_SUBSCRIPTION = "aws_neptune_event_subscription"
    AWS_NEPTUNE_PARAMETER_GROUP = "aws_neptune_parameter_group"
    AWS_NEPTUNE_SUBNET_GROUP = "aws_neptune_subnet_group"
    AWS_NETWORKFIREWALL_FIREWALL = "aws_networkfirewall_firewall"
    AWS_NETWORKFIREWALL_FIREWALL_POLICY = "aws_networkfirewall_firewall_policy"
    AWS_NETWORKFIREWALL_LOGGING_CONFIGURATION = "aws_networkfirewall_logging_configuration"
    AWS_NETWORKFIREWALL_RESOURCE_POLICY = "aws_networkfirewall_resource_policy"
    AWS_NETWORKFIREWALL_RULE_GROUP = "aws_networkfirewall_rule_group"
    AWS_NETWORKMANAGER_ATTACHMENT_ACCEPTER = "aws_networkmanager_attachment_accepter"
    AWS_NETWORKMANAGER_CONNECT_ATTACHMENT = "aws_networkmanager_connect_attachment"
    AWS_NETWORKMANAGER_CONNECTION = "aws_networkmanager_connection"
    AWS_NETWORKMANAGER_CUSTOMER_GATEWAY_ASSOCIATION = "aws_networkmanager_customer_gateway_association"
    AWS_NETWORKMANAGER_DEVICE = "aws_networkmanager_device"
    AWS_NETWORKMANAGER_GLOBAL_NETWORK = "aws_networkmanager_global_network"
    AWS_NETWORKMANAGER_LINK = "aws_networkmanager_link"
    AWS_NETWORKMANAGER_LINK_ASSOCIATION = "aws_networkmanager_link_association"
    AWS_NETWORKMANAGER_SITE = "aws_networkmanager_site"
    AWS_NETWORKMANAGER_SITE_TO_SITE_VPN_ATTACHMENT = "aws_networkmanager_site_to_site_vpn_attachment"
    AWS_NETWORKMANAGER_TRANSIT_GATEWAY_CONNECT_PEER_ASSOCIATION = "aws_networkmanager_transit_gateway_connect_peer_association"
    AWS_NETWORKMANAGER_TRANSIT_GATEWAY_PEERING = "aws_networkmanager_transit_gateway_peering"
    AWS_NETWORKMANAGER_TRANSIT_GATEWAY_REGISTRATION = "aws_networkmanager_transit_gateway_registration"
    AWS_NETWORKMANAGER_TRANSIT_GATEWAY_ROUTE_TABLE_ATTACHMENT = "aws_networkmanager_transit_gateway_route_table_attachment"
    AWS_NETWORKMANAGER_VPC_ATTACHMENT = "aws_networkmanager_vpc_attachment"

    # OpenSearch
    AWS_OPENSEARCH_DOMAIN = "aws_opensearch_domain"
    AWS_OPENSEARCH_DOMAIN_POLICY = "aws_opensearch_domain_policy"
    AWS_OPENSEARCH_DOMAIN_SAML_OPTIONS = "aws_opensearch_domain_saml_options"
    AWS_OPENSEARCH_INBOUND_CONNECTION_ACCEPTER = "aws_opensearch_inbound_connection_accepter"
    AWS_OPENSEARCH_OUTBOUND_CONNECTION = "aws_opensearch_outbound_connection"

    # OpsWorks
    AWS_OPSWORKS_APPLICATION = "aws_opsworks_application"
    AWS_OPSWORKS_CUSTOM_LAYER = "aws_opsworks_custom_layer"
    AWS_OPSWORKS_ECS_CLUSTER_LAYER = "aws_opsworks_ecs_cluster_layer"
    AWS_OPSWORKS_GANGLIA_LAYER = "aws_opsworks_ganglia_layer"
    AWS_OPSWORKS_HAPROXY_LAYER = "aws_opsworks_haproxy_layer"
    AWS_OPSWORKS_INSTANCE = "aws_opsworks_instance"
    AWS_OPSWORKS_JAVA_APP_LAYER = "aws_opsworks_java_app_layer"
    AWS_OPSWORKS_MEMCACHED_LAYER = "aws_opsworks_memcached_layer"
    AWS_OPSWORKS_MYSQL_LAYER = "aws_opsworks_mysql_layer"
    AWS_OPSWORKS_NODEJS_APP_LAYER = "aws_opsworks_nodejs_app_layer"
    AWS_OPSWORKS_PERMISSION = "aws_opsworks_permission"
    AWS_OPSWORKS_PHP_APP_LAYER = "aws_opsworks_php_app_layer"
    AWS_OPSWORKS_RAILS_APP_LAYER = "aws_opsworks_rails_app_layer"
    AWS_OPSWORKS_RDS_DB_INSTANCE = "aws_opsworks_rds_db_instance"
    AWS_OPSWORKS_STACK = "aws_opsworks_stack"
    AWS_OPSWORKS_STATIC_WEB_LAYER = "aws_opsworks_static_web_layer"
    AWS_OPSWORKS_USER_PROFILE = "aws_opsworks_user_profile"

    # Organizations
    AWS_ORGANIZATIONS_ACCOUNT = "aws_organizations_account"
    AWS_ORGANIZATIONS_DELEGATED_ADMINISTRATOR = "aws_organizations_delegated_administrator"
    AWS_ORGANIZATIONS_ORGANIZATION = "aws_organizations_organization"
    AWS_ORGANIZATIONS_ORGANIZATIONAL_UNIT = "aws_organizations_organizational_unit"
    AWS_ORGANIZATIONS_POLICY = "aws_organizations_policy"
    AWS_ORGANIZATIONS_POLICY_ATTACHMENT = "aws_organizations_policy_attachment"

    # Outposts

    # Outposts (EC2)
    AWS_EC2_LOCAL_GATEWAY_ROUTE = "aws_ec2_local_gateway_route"
    AWS_EC2_LOCAL_GATEWAY_ROUTE_TABLE_VPC_ASSOCIATION = "aws_ec2_local_gateway_route_table_vpc_association"

    # Pinpoint
    AWS_PINPOINT_ADM_CHANNEL = "aws_pinpoint_adm_channel"
    AWS_PINPOINT_APNS_CHANNEL = "aws_pinpoint_apns_channel"
    AWS_PINPOINT_APNS_SANDBOX_CHANNEL = "aws_pinpoint_apns_sandbox_channel"
    AWS_PINPOINT_APNS_VOIP_CHANNEL = "aws_pinpoint_apns_voip_channel"
    AWS_PINPOINT_APNS_VOIP_SANDBOX_CHANNEL = "aws_pinpoint_apns_voip_sandbox_channel"
    AWS_PINPOINT_APP = "aws_pinpoint_app"
    AWS_PINPOINT_BAIDU_CHANNEL = "aws_pinpoint_baidu_channel"
    AWS_PINPOINT_EMAIL_CHANNEL = "aws_pinpoint_email_channel"
    AWS_PINPOINT_EVENT_STREAM = "aws_pinpoint_event_stream"
    AWS_PINPOINT_GCM_CHANNEL = "aws_pinpoint_gcm_channel"
    AWS_PINPOINT_SMS_CHANNEL = "aws_pinpoint_sms_channel"

    # QLDB (Quantum Ledger Database)
    AWS_QLDB_LEDGER = "aws_qldb_ledger"
    AWS_QLDB_STREAM = "aws_qldb_stream"

    # QuickSight
    AWS_QUICKSIGHT_DATA_SOURCE = "aws_quicksight_data_source"
    AWS_QUICKSIGHT_GROUP = "aws_quicksight_group"
    AWS_QUICKSIGHT_GROUP_MEMBERSHIP = "aws_quicksight_group_membership"
    AWS_QUICKSIGHT_USER = "aws_quicksight_user"

    # RAM (Resource Access Manager)
    AWS_RAM_PRINCIPAL_ASSOCIATION = "aws_ram_principal_association"
    AWS_RAM_RESOURCE_ASSOCIATION = "aws_ram_resource_association"
    AWS_RAM_RESOURCE_SHARE = "aws_ram_resource_share"
    AWS_RAM_RESOURCE_SHARE_ACCEPTER = "aws_ram_resource_share_accepter"

    # RDS (Relational Database)
    AWS_DB_CLUSTER_SNAPSHOT = "aws_db_cluster_snapshot"
    AWS_DB_EVENT_SUBSCRIPTION = "aws_db_event_subscription"
    AWS_DB_INSTANCE = "aws_db_instance"
    AWS_DB_INSTANCE_AUTOMATED_BACKUPS_REPLICATION = "aws_db_instance_automated_backups_replication"
    AWS_DB_INSTANCE_ROLE_ASSOCIATION = "aws_db_instance_role_association"
    AWS_DB_OPTION_GROUP = "aws_db_option_group"
    AWS_DB_PARAMETER_GROUP = "aws_db_parameter_group"
    AWS_DB_PROXY = "aws_db_proxy"
    AWS_DB_PROXY_DEFAULT_TARGET_GROUP = "aws_db_proxy_default_target_group"
    AWS_DB_PROXY_ENDPOINT = "aws_db_proxy_endpoint"
    AWS_DB_PROXY_TARGET = "aws_db_proxy_target"
    AWS_DB_SECURITY_GROUP = "aws_db_security_group"
    AWS_DB_SNAPSHOT = "aws_db_snapshot"
    AWS_DB_SNAPSHOT_COPY = "aws_db_snapshot_copy"
    AWS_DB_SUBNET_GROUP = "aws_db_subnet_group"
    AWS_RDS_CLUSTER = "aws_rds_cluster"
    AWS_RDS_CLUSTER_ACTIVITY_STREAM = "aws_rds_cluster_activity_stream"
    AWS_RDS_CLUSTER_ENDPOINT = "aws_rds_cluster_endpoint"
    AWS_RDS_CLUSTER_INSTANCE = "aws_rds_cluster_instance"
    AWS_RDS_CLUSTER_PARAMETER_GROUP = "aws_rds_cluster_parameter_group"
    AWS_RDS_CLUSTER_ROLE_ASSOCIATION = "aws_rds_cluster_role_association"
    AWS_RDS_GLOBAL_CLUSTER = "aws_rds_global_cluster"
    AWS_RDS_RESERVED_INSTANCE = "aws_rds_reserved_instance"

    # Redshift
    AWS_REDSHIFT_AUTHENTICATION_PROFILE = "aws_redshift_authentication_profile"
    AWS_REDSHIFT_CLUSTER = "aws_redshift_cluster"
    AWS_REDSHIFT_CLUSTER_IAM_ROLES = "aws_redshift_cluster_iam_roles"
    AWS_REDSHIFT_ENDPOINT_ACCESS = "aws_redshift_endpoint_access"
    AWS_REDSHIFT_ENDPOINT_AUTHORIZATION = "aws_redshift_endpoint_authorization"
    AWS_REDSHIFT_EVENT_SUBSCRIPTION = "aws_redshift_event_subscription"
    AWS_REDSHIFT_HSM_CLIENT_CERTIFICATE = "aws_redshift_hsm_client_certificate"
    AWS_REDSHIFT_HSM_CONFIGURATION = "aws_redshift_hsm_configuration"
    AWS_REDSHIFT_PARAMETER_GROUP = "aws_redshift_parameter_group"
    AWS_REDSHIFT_PARTNER = "aws_redshift_partner"
    AWS_REDSHIFT_SCHEDULED_ACTION = "aws_redshift_scheduled_action"
    AWS_REDSHIFT_SECURITY_GROUP = "aws_redshift_security_group"
    AWS_REDSHIFT_SNAPSHOT_COPY_GRANT = "aws_redshift_snapshot_copy_grant"
    AWS_REDSHIFT_SNAPSHOT_SCHEDULE = "aws_redshift_snapshot_schedule"
    AWS_REDSHIFT_SNAPSHOT_SCHEDULE_ASSOCIATION = "aws_redshift_snapshot_schedule_association"
    AWS_REDSHIFT_SUBNET_GROUP = "aws_redshift_subnet_group"
    AWS_REDSHIFT_USAGE_LIMIT = "aws_redshift_usage_limit"

    # Redshift Data
    AWS_REDSHIFTDATA_STATEMENT = "aws_redshiftdata_statement"
    AWS_REDSHIFTSERVERLESS_ENDPOINT_ACCESS = "aws_redshiftserverless_endpoint_access"
    AWS_REDSHIFTSERVERLESS_NAMESPACE = "aws_redshiftserverless_namespace"
    AWS_REDSHIFTSERVERLESS_SNAPSHOT = "aws_redshiftserverless_snapshot"
    AWS_REDSHIFTSERVERLESS_USAGE_LIMIT = "aws_redshiftserverless_usage_limit"
    AWS_REDSHIFTSERVERLESS_WORKGROUP = "aws_redshiftserverless_workgroup"
    AWS_RESOURCEGROUPS_GROUP = "aws_resourcegroups_group"

    # Resource Groups Tagging

    # Roles Anywhere
    AWS_ROLESANYWHERE_PROFILE = "aws_rolesanywhere_profile"
    AWS_ROLESANYWHERE_TRUST_ANCHOR = "aws_rolesanywhere_trust_anchor"

    # Route 53
    AWS_ROUTE53_DELEGATION_SET = "aws_route53_delegation_set"
    AWS_ROUTE53_HEALTH_CHECK = "aws_route53_health_check"
    AWS_ROUTE53_HOSTED_ZONE_DNSSEC = "aws_route53_hosted_zone_dnssec"
    AWS_ROUTE53_KEY_SIGNING_KEY = "aws_route53_key_signing_key"
    AWS_ROUTE53_QUERY_LOG = "aws_route53_query_log"
    AWS_ROUTE53_RECORD = "aws_route53_record"
    AWS_ROUTE53_TRAFFIC_POLICY = "aws_route53_traffic_policy"
    AWS_ROUTE53_TRAFFIC_POLICY_INSTANCE = "aws_route53_traffic_policy_instance"
    AWS_ROUTE53_VPC_ASSOCIATION_AUTHORIZATION = "aws_route53_vpc_association_authorization"
    AWS_ROUTE53_ZONE = "aws_route53_zone"
    AWS_ROUTE53_ZONE_ASSOCIATION = "aws_route53_zone_association"
    AWS_ROUTE53DOMAINS_REGISTERED_DOMAIN = "aws_route53domains_registered_domain"

    # Route 53 Recovery Control Config
    AWS_ROUTE53RECOVERYCONTROLCONFIG_CLUSTER = "aws_route53recoverycontrolconfig_cluster"
    AWS_ROUTE53RECOVERYCONTROLCONFIG_CONTROL_PANEL = "aws_route53recoverycontrolconfig_control_panel"
    AWS_ROUTE53RECOVERYCONTROLCONFIG_ROUTING_CONTROL = "aws_route53recoverycontrolconfig_routing_control"
    AWS_ROUTE53RECOVERYCONTROLCONFIG_SAFETY_RULE = "aws_route53recoverycontrolconfig_safety_rule"

    # Route 53 Recovery Readiness
    AWS_ROUTE53RECOVERYREADINESS_CELL = "aws_route53recoveryreadiness_cell"
    AWS_ROUTE53RECOVERYREADINESS_READINESS_CHECK = "aws_route53recoveryreadiness_readiness_check"
    AWS_ROUTE53RECOVERYREADINESS_RECOVERY_GROUP = "aws_route53recoveryreadiness_recovery_group"
    AWS_ROUTE53RECOVERYREADINESS_RESOURCE_SET = "aws_route53recoveryreadiness_resource_set"
    AWS_ROUTE53_RESOLVER_CONFIG = "aws_route53_resolver_config"
    AWS_ROUTE53_RESOLVER_DNSSEC_CONFIG = "aws_route53_resolver_dnssec_config"
    AWS_ROUTE53_RESOLVER_ENDPOINT = "aws_route53_resolver_endpoint"
    AWS_ROUTE53_RESOLVER_FIREWALL_CONFIG = "aws_route53_resolver_firewall_config"
    AWS_ROUTE53_RESOLVER_FIREWALL_DOMAIN_LIST = "aws_route53_resolver_firewall_domain_list"
    AWS_ROUTE53_RESOLVER_FIREWALL_RULE = "aws_route53_resolver_firewall_rule"
    AWS_ROUTE53_RESOLVER_FIREWALL_RULE_GROUP = "aws_route53_resolver_firewall_rule_group"
    AWS_ROUTE53_RESOLVER_FIREWALL_RULE_GROUP_ASSOCIATION = "aws_route53_resolver_firewall_rule_group_association"
    AWS_ROUTE53_RESOLVER_QUERY_LOG_CONFIG = "aws_route53_resolver_query_log_config"
    AWS_ROUTE53_RESOLVER_QUERY_LOG_CONFIG_ASSOCIATION = "aws_route53_resolver_query_log_config_association"
    AWS_ROUTE53_RESOLVER_RULE = "aws_route53_resolver_rule"
    AWS_ROUTE53_RESOLVER_RULE_ASSOCIATION = "aws_route53_resolver_rule_association"
    AWS_S3_BUCKET = "aws_s3_bucket"
    AWS_S3_BUCKET_ACCELERATE_CONFIGURATION = "aws_s3_bucket_accelerate_configuration"
    AWS_S3_BUCKET_ACL = "aws_s3_bucket_acl"
    AWS_S3_BUCKET_ANALYTICS_CONFIGURATION = "aws_s3_bucket_analytics_configuration"
    AWS_S3_BUCKET_CORS_CONFIGURATION = "aws_s3_bucket_cors_configuration"
    AWS_S3_BUCKET_INTELLIGENT_TIERING_CONFIGURATION = "aws_s3_bucket_intelligent_tiering_configuration"
    AWS_S3_BUCKET_INVENTORY = "aws_s3_bucket_inventory"
    AWS_S3_BUCKET_LIFECYCLE_CONFIGURATION = "aws_s3_bucket_lifecycle_configuration"
    AWS_S3_BUCKET_LOGGING = "aws_s3_bucket_logging"
    AWS_S3_BUCKET_METRIC = "aws_s3_bucket_metric"
    AWS_S3_BUCKET_NOTIFICATION = "aws_s3_bucket_notification"
    AWS_S3_BUCKET_OBJECT = "aws_s3_bucket_object"
    AWS_S3_BUCKET_OBJECT_LOCK_CONFIGURATION = "aws_s3_bucket_object_lock_configuration"
    AWS_S3_BUCKET_OWNERSHIP_CONTROLS = "aws_s3_bucket_ownership_controls"
    AWS_S3_BUCKET_POLICY = "aws_s3_bucket_policy"
    AWS_S3_BUCKET_PUBLIC_ACCESS_BLOCK = "aws_s3_bucket_public_access_block"
    AWS_S3_BUCKET_REPLICATION_CONFIGURATION = "aws_s3_bucket_replication_configuration"
    AWS_S3_BUCKET_REQUEST_PAYMENT_CONFIGURATION = "aws_s3_bucket_request_payment_configuration"
    AWS_S3_BUCKET_SERVER_SIDE_ENCRYPTION_CONFIGURATION = "aws_s3_bucket_server_side_encryption_configuration"
    AWS_S3_BUCKET_VERSIONING = "aws_s3_bucket_versioning"
    AWS_S3_BUCKET_WEBSITE_CONFIGURATION = "aws_s3_bucket_website_configuration"
    AWS_S3_OBJECT = "aws_s3_object"
    AWS_S3_OBJECT_COPY = "aws_s3_object_copy"

    # S3 Control
    AWS_S3_ACCESS_POINT = "aws_s3_access_point"
    AWS_S3_ACCOUNT_PUBLIC_ACCESS_BLOCK = "aws_s3_account_public_access_block"
    AWS_S3CONTROL_ACCESS_POINT_POLICY = "aws_s3control_access_point_policy"
    AWS_S3CONTROL_BUCKET = "aws_s3control_bucket"
    AWS_S3CONTROL_BUCKET_LIFECYCLE_CONFIGURATION = "aws_s3control_bucket_lifecycle_configuration"
    AWS_S3CONTROL_BUCKET_POLICY = "aws_s3control_bucket_policy"
    AWS_S3CONTROL_MULTI_REGION_ACCESS_POINT = "aws_s3control_multi_region_access_point"
    AWS_S3CONTROL_MULTI_REGION_ACCESS_POINT_POLICY = "aws_s3control_multi_region_access_point_policy"
    AWS_S3CONTROL_OBJECT_LAMBDA_ACCESS_POINT = "aws_s3control_object_lambda_access_point"
    AWS_S3CONTROL_OBJECT_LAMBDA_ACCESS_POINT_POLICY = "aws_s3control_object_lambda_access_point_policy"
    AWS_S3CONTROL_STORAGE_LENS_CONFIGURATION = "aws_s3control_storage_lens_configuration"

    # S3 Glacier
    AWS_GLACIER_VAULT = "aws_glacier_vault"
    AWS_GLACIER_VAULT_LOCK = "aws_glacier_vault_lock"

    # S3 on Outposts
    AWS_S3OUTPOSTS_ENDPOINT = "aws_s3outposts_endpoint"

    # SDB (SimpleDB)
    AWS_SIMPLEDB_DOMAIN = "aws_simpledb_domain"
    AWS_SES_ACTIVE_RECEIPT_RULE_SET = "aws_ses_active_receipt_rule_set"
    AWS_SES_CONFIGURATION_SET = "aws_ses_configuration_set"
    AWS_SES_DOMAIN_DKIM = "aws_ses_domain_dkim"
    AWS_SES_DOMAIN_IDENTITY = "aws_ses_domain_identity"
    AWS_SES_DOMAIN_IDENTITY_VERIFICATION = "aws_ses_domain_identity_verification"
    AWS_SES_DOMAIN_MAIL_FROM = "aws_ses_domain_mail_from"
    AWS_SES_EMAIL_IDENTITY = "aws_ses_email_identity"
    AWS_SES_EVENT_DESTINATION = "aws_ses_event_destination"
    AWS_SES_IDENTITY_NOTIFICATION_TOPIC = "aws_ses_identity_notification_topic"
    AWS_SES_IDENTITY_POLICY = "aws_ses_identity_policy"
    AWS_SES_RECEIPT_FILTER = "aws_ses_receipt_filter"
    AWS_SES_RECEIPT_RULE = "aws_ses_receipt_rule"
    AWS_SES_RECEIPT_RULE_SET = "aws_ses_receipt_rule_set"
    AWS_SES_TEMPLATE = "aws_ses_template"

    # SESv2 (Simple Email V2)
    AWS_SESV2_CONFIGURATION_SET = "aws_sesv2_configuration_set"
    AWS_SESV2_DEDICATED_IP_ASSIGNMENT = "aws_sesv2_dedicated_ip_assignment"
    AWS_SESV2_DEDICATED_IP_POOL = "aws_sesv2_dedicated_ip_pool"
    AWS_SESV2_EMAIL_IDENTITY = "aws_sesv2_email_identity"
    AWS_SESV2_EMAIL_IDENTITY_FEEDBACK_ATTRIBUTES = "aws_sesv2_email_identity_feedback_attributes"
    AWS_SESV2_EMAIL_IDENTITY_MAIL_FROM_ATTRIBUTES = "aws_sesv2_email_identity_mail_from_attributes"
    AWS_SFN_ACTIVITY = "aws_sfn_activity"
    AWS_SFN_STATE_MACHINE = "aws_sfn_state_machine"

    # SNS (Simple Notification)
    AWS_SNS_PLATFORM_APPLICATION = "aws_sns_platform_application"
    AWS_SNS_SMS_PREFERENCES = "aws_sns_sms_preferences"
    AWS_SNS_TOPIC = "aws_sns_topic"
    AWS_SNS_TOPIC_POLICY = "aws_sns_topic_policy"
    AWS_SNS_TOPIC_SUBSCRIPTION = "aws_sns_topic_subscription"
    AWS_SQS_QUEUE = "aws_sqs_queue"
    AWS_SQS_QUEUE_POLICY = "aws_sqs_queue_policy"
    AWS_SQS_QUEUE_REDRIVE_ALLOW_POLICY = "aws_sqs_queue_redrive_allow_policy"
    AWS_SQS_QUEUE_REDRIVE_POLICY = "aws_sqs_queue_redrive_policy"

    # SSM (Systems Manager)
    AWS_SSM_ACTIVATION = "aws_ssm_activation"
    AWS_SSM_ASSOCIATION = "aws_ssm_association"
    AWS_SSM_DEFAULT_PATCH_BASELINE = "aws_ssm_default_patch_baseline"
    AWS_SSM_DOCUMENT = "aws_ssm_document"
    AWS_SSM_MAINTENANCE_WINDOW = "aws_ssm_maintenance_window"
    AWS_SSM_MAINTENANCE_WINDOW_TARGET = "aws_ssm_maintenance_window_target"
    AWS_SSM_MAINTENANCE_WINDOW_TASK = "aws_ssm_maintenance_window_task"
    AWS_SSM_PARAMETER = "aws_ssm_parameter"
    AWS_SSM_PATCH_BASELINE = "aws_ssm_patch_baseline"
    AWS_SSM_PATCH_GROUP = "aws_ssm_patch_group"
    AWS_SSM_RESOURCE_DATA_SYNC = "aws_ssm_resource_data_sync"
    AWS_SSM_SERVICE_SETTING = "aws_ssm_service_setting"

    # SSO Admin
    AWS_SSOADMIN_ACCOUNT_ASSIGNMENT = "aws_ssoadmin_account_assignment"
    AWS_SSOADMIN_CUSTOMER_MANAGED_POLICY_ATTACHMENT = "aws_ssoadmin_customer_managed_policy_attachment"
    AWS_SSOADMIN_MANAGED_POLICY_ATTACHMENT = "aws_ssoadmin_managed_policy_attachment"
    AWS_SSOADMIN_PERMISSION_SET = "aws_ssoadmin_permission_set"
    AWS_SSOADMIN_PERMISSION_SET_INLINE_POLICY = "aws_ssoadmin_permission_set_inline_policy"
    AWS_IDENTITYSTORE_GROUP = "aws_identitystore_group"
    AWS_IDENTITYSTORE_GROUP_MEMBERSHIP = "aws_identitystore_group_membership"
    AWS_IDENTITYSTORE_USER = "aws_identitystore_user"

    # SWF (Simple Workflow)
    AWS_SWF_DOMAIN = "aws_swf_domain"

    # SageMaker
    AWS_SAGEMAKER_APP = "aws_sagemaker_app"
    AWS_SAGEMAKER_APP_IMAGE_CONFIG = "aws_sagemaker_app_image_config"
    AWS_SAGEMAKER_CODE_REPOSITORY = "aws_sagemaker_code_repository"
    AWS_SAGEMAKER_DEVICE = "aws_sagemaker_device"
    AWS_SAGEMAKER_DEVICE_FLEET = "aws_sagemaker_device_fleet"
    AWS_SAGEMAKER_DOMAIN = "aws_sagemaker_domain"
    AWS_SAGEMAKER_ENDPOINT = "aws_sagemaker_endpoint"
    AWS_SAGEMAKER_ENDPOINT_CONFIGURATION = "aws_sagemaker_endpoint_configuration"
    AWS_SAGEMAKER_FEATURE_GROUP = "aws_sagemaker_feature_group"
    AWS_SAGEMAKER_FLOW_DEFINITION = "aws_sagemaker_flow_definition"
    AWS_SAGEMAKER_HUMAN_TASK_UI = "aws_sagemaker_human_task_ui"
    AWS_SAGEMAKER_IMAGE = "aws_sagemaker_image"
    AWS_SAGEMAKER_IMAGE_VERSION = "aws_sagemaker_image_version"
    AWS_SAGEMAKER_MODEL = "aws_sagemaker_model"
    AWS_SAGEMAKER_MODEL_PACKAGE_GROUP = "aws_sagemaker_model_package_group"
    AWS_SAGEMAKER_MODEL_PACKAGE_GROUP_POLICY = "aws_sagemaker_model_package_group_policy"
    AWS_SAGEMAKER_NOTEBOOK_INSTANCE = "aws_sagemaker_notebook_instance"
    AWS_SAGEMAKER_NOTEBOOK_INSTANCE_LIFECYCLE_CONFIGURATION = "aws_sagemaker_notebook_instance_lifecycle_configuration"
    AWS_SAGEMAKER_PROJECT = "aws_sagemaker_project"
    AWS_SAGEMAKER_SERVICECATALOG_PORTFOLIO_STATUS = "aws_sagemaker_servicecatalog_portfolio_status"
    AWS_SAGEMAKER_STUDIO_LIFECYCLE_CONFIG = "aws_sagemaker_studio_lifecycle_config"
    AWS_SAGEMAKER_USER_PROFILE = "aws_sagemaker_user_profile"
    AWS_SAGEMAKER_WORKFORCE = "aws_sagemaker_workforce"
    AWS_SAGEMAKER_WORKTEAM = "aws_sagemaker_workteam"
    AWS_SECRETSMANAGER_SECRET = "aws_secretsmanager_secret"
    AWS_SECRETSMANAGER_SECRET_POLICY = "aws_secretsmanager_secret_policy"
    AWS_SECRETSMANAGER_SECRET_ROTATION = "aws_secretsmanager_secret_rotation"
    AWS_SECRETSMANAGER_SECRET_VERSION = "aws_secretsmanager_secret_version"

    # Security Hub
    AWS_SECURITYHUB_ACCOUNT = "aws_securityhub_account"
    AWS_SECURITYHUB_ACTION_TARGET = "aws_securityhub_action_target"
    AWS_SECURITYHUB_FINDING_AGGREGATOR = "aws_securityhub_finding_aggregator"
    AWS_SECURITYHUB_INSIGHT = "aws_securityhub_insight"
    AWS_SECURITYHUB_INVITE_ACCEPTER = "aws_securityhub_invite_accepter"
    AWS_SECURITYHUB_MEMBER = "aws_securityhub_member"
    AWS_SECURITYHUB_ORGANIZATION_ADMIN_ACCOUNT = "aws_securityhub_organization_admin_account"
    AWS_SECURITYHUB_ORGANIZATION_CONFIGURATION = "aws_securityhub_organization_configuration"
    AWS_SECURITYHUB_PRODUCT_SUBSCRIPTION = "aws_securityhub_product_subscription"
    AWS_SECURITYHUB_STANDARDS_CONTROL = "aws_securityhub_standards_control"
    AWS_SECURITYHUB_STANDARDS_SUBSCRIPTION = "aws_securityhub_standards_subscription"

    # Serverless Application Repository
    AWS_SERVERLESSAPPLICATIONREPOSITORY_CLOUDFORMATION_STACK = "aws_serverlessapplicationrepository_cloudformation_stack"
    AWS_SERVICECATALOG_BUDGET_RESOURCE_ASSOCIATION = "aws_servicecatalog_budget_resource_association"
    AWS_SERVICECATALOG_CONSTRAINT = "aws_servicecatalog_constraint"
    AWS_SERVICECATALOG_ORGANIZATIONS_ACCESS = "aws_servicecatalog_organizations_access"
    AWS_SERVICECATALOG_PORTFOLIO = "aws_servicecatalog_portfolio"
    AWS_SERVICECATALOG_PORTFOLIO_SHARE = "aws_servicecatalog_portfolio_share"
    AWS_SERVICECATALOG_PRINCIPAL_PORTFOLIO_ASSOCIATION = "aws_servicecatalog_principal_portfolio_association"
    AWS_SERVICECATALOG_PRODUCT = "aws_servicecatalog_product"
    AWS_SERVICECATALOG_PRODUCT_PORTFOLIO_ASSOCIATION = "aws_servicecatalog_product_portfolio_association"
    AWS_SERVICECATALOG_PROVISIONED_PRODUCT = "aws_servicecatalog_provisioned_product"
    AWS_SERVICECATALOG_PROVISIONING_ARTIFACT = "aws_servicecatalog_provisioning_artifact"
    AWS_SERVICECATALOG_SERVICE_ACTION = "aws_servicecatalog_service_action"
    AWS_SERVICECATALOG_TAG_OPTION = "aws_servicecatalog_tag_option"
    AWS_SERVICECATALOG_TAG_OPTION_RESOURCE_ASSOCIATION = "aws_servicecatalog_tag_option_resource_association"

    # Service Quotas
    AWS_SERVICEQUOTAS_SERVICE_QUOTA = "aws_servicequotas_service_quota"

    # Shield
    AWS_SHIELD_PROTECTION = "aws_shield_protection"
    AWS_SHIELD_PROTECTION_GROUP = "aws_shield_protection_group"
    AWS_SHIELD_PROTECTION_HEALTH_CHECK_ASSOCIATION = "aws_shield_protection_health_check_association"

    # Signer
    AWS_SIGNER_SIGNING_JOB = "aws_signer_signing_job"
    AWS_SIGNER_SIGNING_PROFILE = "aws_signer_signing_profile"
    AWS_SIGNER_SIGNING_PROFILE_PERMISSION = "aws_signer_signing_profile_permission"
    AWS_STORAGEGATEWAY_CACHE = "aws_storagegateway_cache"
    AWS_STORAGEGATEWAY_CACHED_ISCSI_VOLUME = "aws_storagegateway_cached_iscsi_volume"
    AWS_STORAGEGATEWAY_FILE_SYSTEM_ASSOCIATION = "aws_storagegateway_file_system_association"
    AWS_STORAGEGATEWAY_GATEWAY = "aws_storagegateway_gateway"
    AWS_STORAGEGATEWAY_NFS_FILE_SHARE = "aws_storagegateway_nfs_file_share"
    AWS_STORAGEGATEWAY_SMB_FILE_SHARE = "aws_storagegateway_smb_file_share"
    AWS_STORAGEGATEWAY_STORED_ISCSI_VOLUME = "aws_storagegateway_stored_iscsi_volume"
    AWS_STORAGEGATEWAY_TAPE_POOL = "aws_storagegateway_tape_pool"
    AWS_STORAGEGATEWAY_UPLOAD_BUFFER = "aws_storagegateway_upload_buffer"
    AWS_STORAGEGATEWAY_WORKING_STORAGE = "aws_storagegateway_working_storage"
    AWS_TIMESTREAMWRITE_DATABASE = "aws_timestreamwrite_database"
    AWS_TIMESTREAMWRITE_TABLE = "aws_timestreamwrite_table"

    # Transcribe
    AWS_TRANSCRIBE_LANGUAGE_MODEL = "aws_transcribe_language_model"
    AWS_TRANSCRIBE_MEDICAL_VOCABULARY = "aws_transcribe_medical_vocabulary"
    AWS_TRANSCRIBE_VOCABULARY = "aws_transcribe_vocabulary"
    AWS_TRANSCRIBE_VOCABULARY_FILTER = "aws_transcribe_vocabulary_filter"
    AWS_TRANSFER_ACCESS = "aws_transfer_access"
    AWS_TRANSFER_SERVER = "aws_transfer_server"
    AWS_TRANSFER_SSH_KEY = "aws_transfer_ssh_key"
    AWS_TRANSFER_TAG = "aws_transfer_tag"
    AWS_TRANSFER_USER = "aws_transfer_user"
    AWS_TRANSFER_WORKFLOW = "aws_transfer_workflow"
    AWS_EC2_TRANSIT_GATEWAY = "aws_ec2_transit_gateway"
    AWS_EC2_TRANSIT_GATEWAY_CONNECT = "aws_ec2_transit_gateway_connect"
    AWS_EC2_TRANSIT_GATEWAY_CONNECT_PEER = "aws_ec2_transit_gateway_connect_peer"
    AWS_EC2_TRANSIT_GATEWAY_MULTICAST_DOMAIN = "aws_ec2_transit_gateway_multicast_domain"
    AWS_EC2_TRANSIT_GATEWAY_MULTICAST_DOMAIN_ASSOCIATION = "aws_ec2_transit_gateway_multicast_domain_association"
    AWS_EC2_TRANSIT_GATEWAY_MULTICAST_GROUP_MEMBER = "aws_ec2_transit_gateway_multicast_group_member"
    AWS_EC2_TRANSIT_GATEWAY_MULTICAST_GROUP_SOURCE = "aws_ec2_transit_gateway_multicast_group_source"
    AWS_EC2_TRANSIT_GATEWAY_PEERING_ATTACHMENT = "aws_ec2_transit_gateway_peering_attachment"
    AWS_EC2_TRANSIT_GATEWAY_PEERING_ATTACHMENT_ACCEPTER = "aws_ec2_transit_gateway_peering_attachment_accepter"
    AWS_EC2_TRANSIT_GATEWAY_POLICY_TABLE = "aws_ec2_transit_gateway_policy_table"
    AWS_EC2_TRANSIT_GATEWAY_POLICY_TABLE_ASSOCIATION = "aws_ec2_transit_gateway_policy_table_association"
    AWS_EC2_TRANSIT_GATEWAY_PREFIX_LIST_REFERENCE = "aws_ec2_transit_gateway_prefix_list_reference"
    AWS_EC2_TRANSIT_GATEWAY_ROUTE = "aws_ec2_transit_gateway_route"
    AWS_EC2_TRANSIT_GATEWAY_ROUTE_TABLE = "aws_ec2_transit_gateway_route_table"
    AWS_EC2_TRANSIT_GATEWAY_ROUTE_TABLE_ASSOCIATION = "aws_ec2_transit_gateway_route_table_association"
    AWS_EC2_TRANSIT_GATEWAY_ROUTE_TABLE_PROPAGATION = "aws_ec2_transit_gateway_route_table_propagation"
    AWS_EC2_TRANSIT_GATEWAY_VPC_ATTACHMENT = "aws_ec2_transit_gateway_vpc_attachment"
    AWS_EC2_TRANSIT_GATEWAY_VPC_ATTACHMENT_ACCEPTER = "aws_ec2_transit_gateway_vpc_attachment_accepter"

    # VPC (Virtual Private Cloud)
    AWS_DEFAULT_NETWORK_ACL = "aws_default_network_acl"
    AWS_DEFAULT_ROUTE_TABLE = "aws_default_route_table"
    AWS_DEFAULT_SECURITY_GROUP = "aws_default_security_group"
    AWS_DEFAULT_SUBNET = "aws_default_subnet"
    AWS_DEFAULT_VPC = "aws_default_vpc"
    AWS_DEFAULT_VPC_DHCP_OPTIONS = "aws_default_vpc_dhcp_options"
    AWS_EC2_MANAGED_PREFIX_LIST = "aws_ec2_managed_prefix_list"
    AWS_EC2_MANAGED_PREFIX_LIST_ENTRY = "aws_ec2_managed_prefix_list_entry"
    AWS_EC2_NETWORK_INSIGHTS_ANALYSIS = "aws_ec2_network_insights_analysis"
    AWS_EC2_NETWORK_INSIGHTS_PATH = "aws_ec2_network_insights_path"
    AWS_EC2_SUBNET_CIDR_RESERVATION = "aws_ec2_subnet_cidr_reservation"
    AWS_EC2_TRAFFIC_MIRROR_FILTER = "aws_ec2_traffic_mirror_filter"
    AWS_EC2_TRAFFIC_MIRROR_FILTER_RULE = "aws_ec2_traffic_mirror_filter_rule"
    AWS_EC2_TRAFFIC_MIRROR_SESSION = "aws_ec2_traffic_mirror_session"
    AWS_EC2_TRAFFIC_MIRROR_TARGET = "aws_ec2_traffic_mirror_target"
    AWS_EGRESS_ONLY_INTERNET_GATEWAY = "aws_egress_only_internet_gateway"
    AWS_FLOW_LOG = "aws_flow_log"
    AWS_INTERNET_GATEWAY = "aws_internet_gateway"
    AWS_INTERNET_GATEWAY_ATTACHMENT = "aws_internet_gateway_attachment"
    AWS_MAIN_ROUTE_TABLE_ASSOCIATION = "aws_main_route_table_association"
    AWS_NAT_GATEWAY = "aws_nat_gateway"
    AWS_NETWORK_ACL = "aws_network_acl"
    AWS_NETWORK_ACL_ASSOCIATION = "aws_network_acl_association"
    AWS_NETWORK_ACL_RULE = "aws_network_acl_rule"
    AWS_NETWORK_INTERFACE = "aws_network_interface"
    AWS_NETWORK_INTERFACE_ATTACHMENT = "aws_network_interface_attachment"
    AWS_NETWORK_INTERFACE_SG_ATTACHMENT = "aws_network_interface_sg_attachment"
    AWS_ROUTE = "aws_route"
    AWS_ROUTE_TABLE = "aws_route_table"
    AWS_ROUTE_TABLE_ASSOCIATION = "aws_route_table_association"
    AWS_SECURITY_GROUP = "aws_security_group"
    AWS_SECURITY_GROUP_RULE = "aws_security_group_rule"
    AWS_SUBNET = "aws_subnet"
    AWS_VPC = "aws_vpc"
    AWS_VPC_DHCP_OPTIONS = "aws_vpc_dhcp_options"
    AWS_VPC_DHCP_OPTIONS_ASSOCIATION = "aws_vpc_dhcp_options_association"
    AWS_VPC_ENDPOINT = "aws_vpc_endpoint"
    AWS_VPC_ENDPOINT_CONNECTION_ACCEPTER = "aws_vpc_endpoint_connection_accepter"
    AWS_VPC_ENDPOINT_CONNECTION_NOTIFICATION = "aws_vpc_endpoint_connection_notification"
    AWS_VPC_ENDPOINT_POLICY = "aws_vpc_endpoint_policy"
    AWS_VPC_ENDPOINT_ROUTE_TABLE_ASSOCIATION = "aws_vpc_endpoint_route_table_association"
    AWS_VPC_ENDPOINT_SECURITY_GROUP_ASSOCIATION = "aws_vpc_endpoint_security_group_association"
    AWS_VPC_ENDPOINT_SERVICE = "aws_vpc_endpoint_service"
    AWS_VPC_ENDPOINT_SERVICE_ALLOWED_PRINCIPAL = "aws_vpc_endpoint_service_allowed_principal"
    AWS_VPC_ENDPOINT_SUBNET_ASSOCIATION = "aws_vpc_endpoint_subnet_association"
    AWS_VPC_IPV4_CIDR_BLOCK_ASSOCIATION = "aws_vpc_ipv4_cidr_block_association"
    AWS_VPC_IPV6_CIDR_BLOCK_ASSOCIATION = "aws_vpc_ipv6_cidr_block_association"
    AWS_VPC_PEERING_CONNECTION = "aws_vpc_peering_connection"
    AWS_VPC_PEERING_CONNECTION_ACCEPTER = "aws_vpc_peering_connection_accepter"
    AWS_VPC_PEERING_CONNECTION_OPTIONS = "aws_vpc_peering_connection_options"

    # VPC IPAM (IP Address Manager)
    AWS_VPC_IPAM = "aws_vpc_ipam"
    AWS_VPC_IPAM_ORGANIZATION_ADMIN_ACCOUNT = "aws_vpc_ipam_organization_admin_account"
    AWS_VPC_IPAM_POOL = "aws_vpc_ipam_pool"
    AWS_VPC_IPAM_POOL_CIDR = "aws_vpc_ipam_pool_cidr"
    AWS_VPC_IPAM_POOL_CIDR_ALLOCATION = "aws_vpc_ipam_pool_cidr_allocation"
    AWS_VPC_IPAM_PREVIEW_NEXT_CIDR = "aws_vpc_ipam_preview_next_cidr"
    AWS_VPC_IPAM_SCOPE = "aws_vpc_ipam_scope"

    # VPN (Client)
    AWS_EC2_CLIENT_VPN_AUTHORIZATION_RULE = "aws_ec2_client_vpn_authorization_rule"
    AWS_EC2_CLIENT_VPN_ENDPOINT = "aws_ec2_client_vpn_endpoint"
    AWS_EC2_CLIENT_VPN_NETWORK_ASSOCIATION = "aws_ec2_client_vpn_network_association"
    AWS_EC2_CLIENT_VPN_ROUTE = "aws_ec2_client_vpn_route"
    AWS_CUSTOMER_GATEWAY = "aws_customer_gateway"
    AWS_VPN_CONNECTION = "aws_vpn_connection"
    AWS_VPN_CONNECTION_ROUTE = "aws_vpn_connection_route"
    AWS_VPN_GATEWAY = "aws_vpn_gateway"
    AWS_VPN_GATEWAY_ATTACHMENT = "aws_vpn_gateway_attachment"
    AWS_VPN_GATEWAY_ROUTE_PROPAGATION = "aws_vpn_gateway_route_propagation"

    # WAF
    AWS_WAFV2_IP_SET = "aws_wafv2_ip_set"
    AWS_WAFV2_REGEX_PATTERN_SET = "aws_wafv2_regex_pattern_set"
    AWS_WAFV2_RULE_GROUP = "aws_wafv2_rule_group"
    AWS_WAFV2_WEB_ACL = "aws_wafv2_web_acl"
    AWS_WAFV2_WEB_ACL_ASSOCIATION = "aws_wafv2_web_acl_association"
    AWS_WAFV2_WEB_ACL_LOGGING_CONFIGURATION = "aws_wafv2_web_acl_logging_configuration"

    # WAF Classic
    AWS_WAF_BYTE_MATCH_SET = "aws_waf_byte_match_set"
    AWS_WAF_GEO_MATCH_SET = "aws_waf_geo_match_set"
    AWS_WAF_IPSET = "aws_waf_ipset"
    AWS_WAF_RATE_BASED_RULE = "aws_waf_rate_based_rule"
    AWS_WAF_REGEX_MATCH_SET = "aws_waf_regex_match_set"
    AWS_WAF_REGEX_PATTERN_SET = "aws_waf_regex_pattern_set"
    AWS_WAF_RULE = "aws_waf_rule"
    AWS_WAF_RULE_GROUP = "aws_waf_rule_group"
    AWS_WAF_SIZE_CONSTRAINT_SET = "aws_waf_size_constraint_set"
    AWS_WAF_SQL_INJECTION_MATCH_SET = "aws_waf_sql_injection_match_set"
    AWS_WAF_WEB_ACL = "aws_waf_web_acl"
    AWS_WAF_XSS_MATCH_SET = "aws_waf_xss_match_set"
    AWS_WAFREGIONAL_BYTE_MATCH_SET = "aws_wafregional_byte_match_set"
    AWS_WAFREGIONAL_GEO_MATCH_SET = "aws_wafregional_geo_match_set"
    AWS_WAFREGIONAL_IPSET = "aws_wafregional_ipset"
    AWS_WAFREGIONAL_RATE_BASED_RULE = "aws_wafregional_rate_based_rule"
    AWS_WAFREGIONAL_REGEX_MATCH_SET = "aws_wafregional_regex_match_set"
    AWS_WAFREGIONAL_REGEX_PATTERN_SET = "aws_wafregional_regex_pattern_set"
    AWS_WAFREGIONAL_RULE = "aws_wafregional_rule"
    AWS_WAFREGIONAL_RULE_GROUP = "aws_wafregional_rule_group"
    AWS_WAFREGIONAL_SIZE_CONSTRAINT_SET = "aws_wafregional_size_constraint_set"
    AWS_WAFREGIONAL_SQL_INJECTION_MATCH_SET = "aws_wafregional_sql_injection_match_set"
    AWS_WAFREGIONAL_WEB_ACL = "aws_wafregional_web_acl"
    AWS_WAFREGIONAL_WEB_ACL_ASSOCIATION = "aws_wafregional_web_acl_association"
    AWS_WAFREGIONAL_XSS_MATCH_SET = "aws_wafregional_xss_match_set"

    # Wavelength
    AWS_EC2_CARRIER_GATEWAY = "aws_ec2_carrier_gateway"
    AWS_BUDGETS_BUDGET = "aws_budgets_budget"
    AWS_BUDGETS_BUDGET_ACTION = "aws_budgets_budget_action"

    # WorkLink
    AWS_WORKLINK_FLEET = "aws_worklink_fleet"
    AWS_WORKLINK_WEBSITE_CERTIFICATE_AUTHORITY_ASSOCIATION = "aws_worklink_website_certificate_authority_association"

    # WorkSpaces
    AWS_WORKSPACES_DIRECTORY = "aws_workspaces_directory"
    AWS_WORKSPACES_IP_GROUP = "aws_workspaces_ip_group"
    AWS_WORKSPACES_WORKSPACE = "aws_workspaces_workspace"

    # X-Ray
    AWS_XRAY_ENCRYPTION_CONFIG = "aws_xray_encryption_config"
    AWS_XRAY_GROUP = "aws_xray_group"
    AWS_XRAY_SAMPLING_RULE = "aws_xray_sampling_rule"


class AWSData(str, Enum):
    # ACM
    AWS_ACM_CERTIFICATE = "aws_acm_certificate"

    # ACM PCA
    AWS_ACMPCA_CERTIFICATE = "aws_acmpca_certificate"
    AWS_ACMPCA_CERTIFICATE_AUTHORITY = "aws_acmpca_certificate_authority"

    # AMP
    AWS_PROMETHEUS_WORKSPACE = "aws_prometheus_workspace"

    # API Gateway
    AWS_API_GATEWAY_API_KEY = "aws_api_gateway_api_key"
    AWS_API_GATEWAY_DOMAIN_NAME = "aws_api_gateway_domain_name"
    AWS_API_GATEWAY_EXPORT = "aws_api_gateway_export"
    AWS_API_GATEWAY_RESOURCE = "aws_api_gateway_resource"
    AWS_API_GATEWAY_REST_API = "aws_api_gateway_rest_api"
    AWS_API_GATEWAY_SDK = "aws_api_gateway_sdk"
    AWS_API_GATEWAY_VPC_LINK = "aws_api_gateway_vpc_link"

    # API Gateway V2
    AWS_APIGATEWAYV2_API = "aws_apigatewayv2_api"
    AWS_APIGATEWAYV2_APIS = "aws_apigatewayv2_apis"
    AWS_APIGATEWAYV2_EXPORT = "aws_apigatewayv2_export"

    # App Mesh
    AWS_APPMESH_MESH = "aws_appmesh_mesh"
    AWS_APPMESH_VIRTUAL_SERVICE = "aws_appmesh_virtual_service"

    # AppConfig
    AWS_APPCONFIG_CONFIGURATION_PROFILE = "aws_appconfig_configuration_profile"
    AWS_APPCONFIG_CONFIGURATION_PROFILES = "aws_appconfig_configuration_profiles"
    AWS_APPCONFIG_ENVIRONMENT = "aws_appconfig_environment"
    AWS_APPCONFIG_ENVIRONMENTS = "aws_appconfig_environments"

    # AppFlow

    # AppStream 2.0

    # AppSync

    # Application Auto Scaling

    # Athena

    # Auto Scaling
    AWS_AUTOSCALING_GROUP = "aws_autoscaling_group"
    AWS_AUTOSCALING_GROUPS = "aws_autoscaling_groups"
    AWS_LAUNCH_CONFIGURATION = "aws_launch_configuration"

    # Backup
    AWS_BACKUP_FRAMEWORK = "aws_backup_framework"
    AWS_BACKUP_PLAN = "aws_backup_plan"
    AWS_BACKUP_REPORT_PLAN = "aws_backup_report_plan"
    AWS_BACKUP_SELECTION = "aws_backup_selection"
    AWS_BACKUP_VAULT = "aws_backup_vault"

    # Batch
    AWS_BATCH_COMPUTE_ENVIRONMENT = "aws_batch_compute_environment"
    AWS_BATCH_JOB_QUEUE = "aws_batch_job_queue"
    AWS_BATCH_SCHEDULING_POLICY = "aws_batch_scheduling_policy"
    AWS_CE_COST_CATEGORY = "aws_ce_cost_category"
    AWS_CE_TAGS = "aws_ce_tags"

    # Chime
    AWS_CLOUDCONTROLAPI_RESOURCE = "aws_cloudcontrolapi_resource"

    # Cloud Map
    AWS_SERVICE_DISCOVERY_DNS_NAMESPACE = "aws_service_discovery_dns_namespace"
    AWS_SERVICE_DISCOVERY_HTTP_NAMESPACE = "aws_service_discovery_http_namespace"
    AWS_SERVICE_DISCOVERY_SERVICE = "aws_service_discovery_service"

    # Cloud9

    # CloudFormation
    AWS_CLOUDFORMATION_EXPORT = "aws_cloudformation_export"
    AWS_CLOUDFORMATION_STACK = "aws_cloudformation_stack"
    AWS_CLOUDFORMATION_TYPE = "aws_cloudformation_type"

    # CloudFront
    AWS_CLOUDFRONT_CACHE_POLICY = "aws_cloudfront_cache_policy"
    AWS_CLOUDFRONT_DISTRIBUTION = "aws_cloudfront_distribution"
    AWS_CLOUDFRONT_FUNCTION = "aws_cloudfront_function"
    AWS_CLOUDFRONT_LOG_DELIVERY_CANONICAL_USER_ID = "aws_cloudfront_log_delivery_canonical_user_id"
    AWS_CLOUDFRONT_ORIGIN_ACCESS_IDENTITIES = "aws_cloudfront_origin_access_identities"
    AWS_CLOUDFRONT_ORIGIN_ACCESS_IDENTITY = "aws_cloudfront_origin_access_identity"
    AWS_CLOUDFRONT_ORIGIN_REQUEST_POLICY = "aws_cloudfront_origin_request_policy"
    AWS_CLOUDFRONT_REALTIME_LOG_CONFIG = "aws_cloudfront_realtime_log_config"
    AWS_CLOUDFRONT_RESPONSE_HEADERS_POLICY = "aws_cloudfront_response_headers_policy"

    # CloudHSM
    AWS_CLOUDHSM_V2_CLUSTER = "aws_cloudhsm_v2_cluster"

    # CloudSearch

    # CloudTrail
    AWS_CLOUDTRAIL_SERVICE_ACCOUNT = "aws_cloudtrail_service_account"

    # CloudWatch

    # CloudWatch Application Insights
    AWS_CLOUDWATCH_LOG_GROUP = "aws_cloudwatch_log_group"
    AWS_CLOUDWATCH_LOG_GROUPS = "aws_cloudwatch_log_groups"

    # CloudWatch RUM

    # CloudWatch Synthetics

    # CodeArtifact
    AWS_CODEARTIFACT_AUTHORIZATION_TOKEN = "aws_codeartifact_authorization_token"
    AWS_CODEARTIFACT_REPOSITORY_ENDPOINT = "aws_codeartifact_repository_endpoint"

    # CodeBuild

    # CodeCommit
    AWS_CODECOMMIT_APPROVAL_RULE_TEMPLATE = "aws_codecommit_approval_rule_template"
    AWS_CODECOMMIT_REPOSITORY = "aws_codecommit_repository"

    # CodeDeploy

    # CodePipeline
    AWS_CODESTARCONNECTIONS_CONNECTION = "aws_codestarconnections_connection"

    # CodeStar Notifications

    # Cognito IDP (Identity Provider)
    AWS_COGNITO_USER_POOL_CLIENT = "aws_cognito_user_pool_client"
    AWS_COGNITO_USER_POOL_CLIENTS = "aws_cognito_user_pool_clients"
    AWS_COGNITO_USER_POOL_SIGNING_CERTIFICATE = "aws_cognito_user_pool_signing_certificate"
    AWS_COGNITO_USER_POOLS = "aws_cognito_user_pools"

    # Comprehend

    # Config

    # Connect
    AWS_CONNECT_BOT_ASSOCIATION = "aws_connect_bot_association"
    AWS_CONNECT_CONTACT_FLOW = "aws_connect_contact_flow"
    AWS_CONNECT_CONTACT_FLOW_MODULE = "aws_connect_contact_flow_module"
    AWS_CONNECT_HOURS_OF_OPERATION = "aws_connect_hours_of_operation"
    AWS_CONNECT_INSTANCE = "aws_connect_instance"
    AWS_CONNECT_INSTANCE_STORAGE_CONFIG = "aws_connect_instance_storage_config"
    AWS_CONNECT_LAMBDA_FUNCTION_ASSOCIATION = "aws_connect_lambda_function_association"
    AWS_CONNECT_PROMPT = "aws_connect_prompt"
    AWS_CONNECT_QUEUE = "aws_connect_queue"
    AWS_CONNECT_QUICK_CONNECT = "aws_connect_quick_connect"
    AWS_CONNECT_ROUTING_PROFILE = "aws_connect_routing_profile"
    AWS_CONNECT_SECURITY_PROFILE = "aws_connect_security_profile"
    AWS_CONNECT_USER_HIERARCHY_GROUP = "aws_connect_user_hierarchy_group"
    AWS_CONNECT_USER_HIERARCHY_STRUCTURE = "aws_connect_user_hierarchy_structure"

    # Control Tower
    AWS_CONTROLTOWER_CONTROLS = "aws_controltower_controls"

    # Cost and Usage Report
    AWS_CUR_REPORT_DEFINITION = "aws_cur_report_definition"

    # DLM (Data Lifecycle Manager)

    # DMS (Database Migration)

    # DS (Directory Service)
    AWS_DIRECTORY_SERVICE_DIRECTORY = "aws_directory_service_directory"

    # Data Exchange

    # Data Pipeline
    AWS_DATAPIPELINE_PIPELINE = "aws_datapipeline_pipeline"
    AWS_DATAPIPELINE_PIPELINE_DEFINITION = "aws_datapipeline_pipeline_definition"

    # DataSync

    # Detective

    # Device Farm

    # Direct Connect
    AWS_DX_CONNECTION = "aws_dx_connection"
    AWS_DX_GATEWAY = "aws_dx_gateway"
    AWS_DX_LOCATION = "aws_dx_location"
    AWS_DX_LOCATIONS = "aws_dx_locations"
    AWS_DX_ROUTER_CONFIGURATION = "aws_dx_router_configuration"
    AWS_DOCDB_ENGINE_VERSION = "aws_docdb_engine_version"
    AWS_DOCDB_ORDERABLE_DB_INSTANCE = "aws_docdb_orderable_db_instance"

    # DynamoDB
    AWS_DYNAMODB_TABLE = "aws_dynamodb_table"
    AWS_DYNAMODB_TABLE_ITEM = "aws_dynamodb_table_item"

    # DynamoDB Accelerator (DAX)

    # EBS (EC2)
    AWS_EBS_DEFAULT_KMS_KEY = "aws_ebs_default_kms_key"
    AWS_EBS_ENCRYPTION_BY_DEFAULT = "aws_ebs_encryption_by_default"
    AWS_EBS_SNAPSHOT = "aws_ebs_snapshot"
    AWS_EBS_SNAPSHOT_IDS = "aws_ebs_snapshot_ids"
    AWS_EBS_VOLUME = "aws_ebs_volume"
    AWS_EBS_VOLUMES = "aws_ebs_volumes"

    # EC2 (Elastic Compute Cloud)
    AWS_AMI = "aws_ami"
    AWS_AMI_IDS = "aws_ami_ids"
    AWS_AVAILABILITY_ZONE = "aws_availability_zone"
    AWS_AVAILABILITY_ZONES = "aws_availability_zones"
    AWS_EC2_HOST = "aws_ec2_host"
    AWS_EC2_INSTANCE_TYPE = "aws_ec2_instance_type"
    AWS_EC2_INSTANCE_TYPE_OFFERING = "aws_ec2_instance_type_offering"
    AWS_EC2_INSTANCE_TYPE_OFFERINGS = "aws_ec2_instance_type_offerings"
    AWS_EC2_INSTANCE_TYPES = "aws_ec2_instance_types"
    AWS_EC2_SERIAL_CONSOLE_ACCESS = "aws_ec2_serial_console_access"
    AWS_EC2_SPOT_PRICE = "aws_ec2_spot_price"
    AWS_EIP = "aws_eip"
    AWS_EIPS = "aws_eips"
    AWS_INSTANCE = "aws_instance"
    AWS_INSTANCES = "aws_instances"
    AWS_KEY_PAIR = "aws_key_pair"
    AWS_LAUNCH_TEMPLATE = "aws_launch_template"
    AWS_IMAGEBUILDER_COMPONENT = "aws_imagebuilder_component"
    AWS_IMAGEBUILDER_COMPONENTS = "aws_imagebuilder_components"
    AWS_IMAGEBUILDER_CONTAINER_RECIPE = "aws_imagebuilder_container_recipe"
    AWS_IMAGEBUILDER_CONTAINER_RECIPES = "aws_imagebuilder_container_recipes"
    AWS_IMAGEBUILDER_DISTRIBUTION_CONFIGURATION = "aws_imagebuilder_distribution_configuration"
    AWS_IMAGEBUILDER_DISTRIBUTION_CONFIGURATIONS = "aws_imagebuilder_distribution_configurations"
    AWS_IMAGEBUILDER_IMAGE = "aws_imagebuilder_image"
    AWS_IMAGEBUILDER_IMAGE_PIPELINE = "aws_imagebuilder_image_pipeline"
    AWS_IMAGEBUILDER_IMAGE_PIPELINES = "aws_imagebuilder_image_pipelines"
    AWS_IMAGEBUILDER_IMAGE_RECIPE = "aws_imagebuilder_image_recipe"
    AWS_IMAGEBUILDER_IMAGE_RECIPES = "aws_imagebuilder_image_recipes"
    AWS_IMAGEBUILDER_INFRASTRUCTURE_CONFIGURATION = "aws_imagebuilder_infrastructure_configuration"
    AWS_IMAGEBUILDER_INFRASTRUCTURE_CONFIGURATIONS = "aws_imagebuilder_infrastructure_configurations"

    # ECR (Elastic Container Registry)
    AWS_ECR_AUTHORIZATION_TOKEN = "aws_ecr_authorization_token"
    AWS_ECR_IMAGE = "aws_ecr_image"
    AWS_ECR_REPOSITORY = "aws_ecr_repository"

    # ECR Public
    AWS_ECRPUBLIC_AUTHORIZATION_TOKEN = "aws_ecrpublic_authorization_token"

    # ECS (Elastic Container)
    AWS_ECS_CLUSTER = "aws_ecs_cluster"
    AWS_ECS_CONTAINER_DEFINITION = "aws_ecs_container_definition"
    AWS_ECS_SERVICE = "aws_ecs_service"
    AWS_ECS_TASK_DEFINITION = "aws_ecs_task_definition"

    # EFS (Elastic File System)
    AWS_EFS_ACCESS_POINT = "aws_efs_access_point"
    AWS_EFS_ACCESS_POINTS = "aws_efs_access_points"
    AWS_EFS_FILE_SYSTEM = "aws_efs_file_system"
    AWS_EFS_MOUNT_TARGET = "aws_efs_mount_target"

    # EKS (Elastic Kubernetes)
    AWS_EKS_ADDON = "aws_eks_addon"
    AWS_EKS_ADDON_VERSION = "aws_eks_addon_version"
    AWS_EKS_CLUSTER = "aws_eks_cluster"
    AWS_EKS_CLUSTER_AUTH = "aws_eks_cluster_auth"
    AWS_EKS_CLUSTERS = "aws_eks_clusters"
    AWS_EKS_NODE_GROUP = "aws_eks_node_group"
    AWS_EKS_NODE_GROUPS = "aws_eks_node_groups"

    # ELB (Elastic Load Balancing)
    AWS_LB = "aws_lb"
    AWS_LB_HOSTED_ZONE_ID = "aws_lb_hosted_zone_id"
    AWS_LB_LISTENER = "aws_lb_listener"
    AWS_LB_TARGET_GROUP = "aws_lb_target_group"

    # ELB Classic
    AWS_ELB = "aws_elb"
    AWS_ELB_HOSTED_ZONE_ID = "aws_elb_hosted_zone_id"
    AWS_ELB_SERVICE_ACCOUNT = "aws_elb_service_account"

    # EMR
    AWS_EMR_RELEASE_LABELS = "aws_emr_release_labels"

    # EMR Containers
    AWS_EMRCONTAINERS_VIRTUAL_CLUSTER = "aws_emrcontainers_virtual_cluster"

    # EMR Serverless

    # ElastiCache
    AWS_ELASTICACHE_CLUSTER = "aws_elasticache_cluster"
    AWS_ELASTICACHE_REPLICATION_GROUP = "aws_elasticache_replication_group"
    AWS_ELASTICACHE_SUBNET_GROUP = "aws_elasticache_subnet_group"
    AWS_ELASTICACHE_USER = "aws_elasticache_user"
    AWS_ELASTIC_BEANSTALK_APPLICATION = "aws_elastic_beanstalk_application"
    AWS_ELASTIC_BEANSTALK_HOSTED_ZONE = "aws_elastic_beanstalk_hosted_zone"
    AWS_ELASTIC_BEANSTALK_SOLUTION_STACK = "aws_elastic_beanstalk_solution_stack"

    # Elasticsearch
    AWS_ELASTICSEARCH_DOMAIN = "aws_elasticsearch_domain"

    # Elemental MediaConvert

    # Elemental MediaPackage

    # EventBridge
    AWS_CLOUDWATCH_EVENT_BUS = "aws_cloudwatch_event_bus"
    AWS_CLOUDWATCH_EVENT_CONNECTION = "aws_cloudwatch_event_connection"
    AWS_CLOUDWATCH_EVENT_SOURCE = "aws_cloudwatch_event_source"

    # EventBridge Scheduler

    # FIS (Fault Injection Simulator)

    # FMS (Firewall Manager)

    # FSx
    AWS_FSX_OPENZFS_SNAPSHOT = "aws_fsx_openzfs_snapshot"

    # GameLift
    AWS_GLOBALACCELERATOR_ACCELERATOR = "aws_globalaccelerator_accelerator"

    # Glue
    AWS_GLUE_CONNECTION = "aws_glue_connection"
    AWS_GLUE_DATA_CATALOG_ENCRYPTION_SETTINGS = "aws_glue_data_catalog_encryption_settings"
    AWS_GLUE_SCRIPT = "aws_glue_script"

    # GuardDuty
    AWS_GUARDDUTY_DETECTOR = "aws_guardduty_detector"

    # IAM (Identity &amp; Access Management)
    AWS_IAM_ACCOUNT_ALIAS = "aws_iam_account_alias"
    AWS_IAM_GROUP = "aws_iam_group"
    AWS_IAM_INSTANCE_PROFILE = "aws_iam_instance_profile"
    AWS_IAM_INSTANCE_PROFILES = "aws_iam_instance_profiles"
    AWS_IAM_OPENID_CONNECT_PROVIDER = "aws_iam_openid_connect_provider"
    AWS_IAM_POLICY = "aws_iam_policy"
    AWS_IAM_POLICY_DOCUMENT = "aws_iam_policy_document"
    AWS_IAM_ROLE = "aws_iam_role"
    AWS_IAM_ROLES = "aws_iam_roles"
    AWS_IAM_SAML_PROVIDER = "aws_iam_saml_provider"
    AWS_IAM_SERVER_CERTIFICATE = "aws_iam_server_certificate"
    AWS_IAM_SESSION_CONTEXT = "aws_iam_session_context"
    AWS_IAM_USER = "aws_iam_user"
    AWS_IAM_USER_SSH_KEY = "aws_iam_user_ssh_key"
    AWS_IAM_USERS = "aws_iam_users"

    # IVS (Interactive Video)
    AWS_IVS_STREAM_KEY = "aws_ivs_stream_key"

    # Inspector
    AWS_INSPECTOR_RULES_PACKAGES = "aws_inspector_rules_packages"

    # Inspector V2

    # IoT Core
    AWS_IOT_ENDPOINT = "aws_iot_endpoint"
    AWS_KMS_ALIAS = "aws_kms_alias"
    AWS_KMS_CIPHERTEXT = "aws_kms_ciphertext"
    AWS_KMS_CUSTOM_KEY_STORE = "aws_kms_custom_key_store"
    AWS_KMS_KEY = "aws_kms_key"
    AWS_KMS_PUBLIC_KEY = "aws_kms_public_key"
    AWS_KMS_SECRET = "aws_kms_secret"
    AWS_KMS_SECRETS = "aws_kms_secrets"

    # Kendra
    AWS_KENDRA_EXPERIENCE = "aws_kendra_experience"
    AWS_KENDRA_FAQ = "aws_kendra_faq"
    AWS_KENDRA_INDEX = "aws_kendra_index"
    AWS_KENDRA_QUERY_SUGGESTIONS_BLOCK_LIST = "aws_kendra_query_suggestions_block_list"
    AWS_KENDRA_THESAURUS = "aws_kendra_thesaurus"

    # Keyspaces (for Apache Cassandra)

    # Kinesis
    AWS_KINESIS_STREAM = "aws_kinesis_stream"
    AWS_KINESIS_STREAM_CONSUMER = "aws_kinesis_stream_consumer"
    AWS_KINESIS_FIREHOSE_DELIVERY_STREAM = "aws_kinesis_firehose_delivery_stream"

    # Kinesis Video

    # Lake Formation
    AWS_LAKEFORMATION_DATA_LAKE_SETTINGS = "aws_lakeformation_data_lake_settings"
    AWS_LAKEFORMATION_PERMISSIONS = "aws_lakeformation_permissions"
    AWS_LAKEFORMATION_RESOURCE = "aws_lakeformation_resource"

    # Lambda
    AWS_LAMBDA_ALIAS = "aws_lambda_alias"
    AWS_LAMBDA_CODE_SIGNING_CONFIG = "aws_lambda_code_signing_config"
    AWS_LAMBDA_FUNCTION = "aws_lambda_function"
    AWS_LAMBDA_FUNCTION_URL = "aws_lambda_function_url"
    AWS_LAMBDA_INVOCATION = "aws_lambda_invocation"
    AWS_LAMBDA_LAYER_VERSION = "aws_lambda_layer_version"
    AWS_LEX_BOT = "aws_lex_bot"
    AWS_LEX_BOT_ALIAS = "aws_lex_bot_alias"
    AWS_LEX_INTENT = "aws_lex_intent"
    AWS_LEX_SLOT_TYPE = "aws_lex_slot_type"

    # Lightsail

    # Location
    AWS_LOCATION_GEOFENCE_COLLECTION = "aws_location_geofence_collection"
    AWS_LOCATION_MAP = "aws_location_map"
    AWS_LOCATION_PLACE_INDEX = "aws_location_place_index"
    AWS_LOCATION_ROUTE_CALCULATOR = "aws_location_route_calculator"
    AWS_LOCATION_TRACKER = "aws_location_tracker"
    AWS_LOCATION_TRACKER_ASSOCIATION = "aws_location_tracker_association"
    AWS_LOCATION_TRACKER_ASSOCIATIONS = "aws_location_tracker_associations"

    # MQ
    AWS_MQ_BROKER = "aws_mq_broker"
    AWS_MQ_BROKER_INSTANCE_TYPE_OFFERINGS = "aws_mq_broker_instance_type_offerings"

    # MWAA (Managed Workflows for Apache Airflow)

    # Macie

    # Macie Classic
    AWS_GRAFANA_WORKSPACE = "aws_grafana_workspace"

    # Managed Streaming for Kafka
    AWS_MSK_BROKER_NODES = "aws_msk_broker_nodes"
    AWS_MSK_CLUSTER = "aws_msk_cluster"
    AWS_MSK_CONFIGURATION = "aws_msk_configuration"
    AWS_MSK_KAFKA_VERSION = "aws_msk_kafka_version"

    # Managed Streaming for Kafka Connect
    AWS_MSKCONNECT_CONNECTOR = "aws_mskconnect_connector"
    AWS_MSKCONNECT_CUSTOM_PLUGIN = "aws_mskconnect_custom_plugin"
    AWS_MSKCONNECT_WORKER_CONFIGURATION = "aws_mskconnect_worker_configuration"
    AWS_MEMORYDB_ACL = "aws_memorydb_acl"
    AWS_MEMORYDB_CLUSTER = "aws_memorydb_cluster"
    AWS_MEMORYDB_PARAMETER_GROUP = "aws_memorydb_parameter_group"
    AWS_MEMORYDB_SNAPSHOT = "aws_memorydb_snapshot"
    AWS_MEMORYDB_SUBNET_GROUP = "aws_memorydb_subnet_group"
    AWS_MEMORYDB_USER = "aws_memorydb_user"
    AWS_ARN = "aws_arn"
    AWS_BILLING_SERVICE_ACCOUNT = "aws_billing_service_account"
    AWS_DEFAULT_TAGS = "aws_default_tags"
    AWS_IP_RANGES = "aws_ip_ranges"
    AWS_PARTITION = "aws_partition"
    AWS_REGION = "aws_region"
    AWS_REGIONS = "aws_regions"
    AWS_SERVICE = "aws_service"

    # Neptune
    AWS_NEPTUNE_ENGINE_VERSION = "aws_neptune_engine_version"
    AWS_NEPTUNE_ORDERABLE_DB_INSTANCE = "aws_neptune_orderable_db_instance"
    AWS_NETWORKFIREWALL_FIREWALL = "aws_networkfirewall_firewall"
    AWS_NETWORKFIREWALL_FIREWALL_POLICY = "aws_networkfirewall_firewall_policy"
    AWS_NETWORKMANAGER_CONNECTION = "aws_networkmanager_connection"
    AWS_NETWORKMANAGER_CONNECTIONS = "aws_networkmanager_connections"
    AWS_NETWORKMANAGER_CORE_NETWORK_POLICY_DOCUMENT = "aws_networkmanager_core_network_policy_document"
    AWS_NETWORKMANAGER_DEVICE = "aws_networkmanager_device"
    AWS_NETWORKMANAGER_DEVICES = "aws_networkmanager_devices"
    AWS_NETWORKMANAGER_GLOBAL_NETWORK = "aws_networkmanager_global_network"
    AWS_NETWORKMANAGER_GLOBAL_NETWORKS = "aws_networkmanager_global_networks"
    AWS_NETWORKMANAGER_LINK = "aws_networkmanager_link"
    AWS_NETWORKMANAGER_LINKS = "aws_networkmanager_links"
    AWS_NETWORKMANAGER_SITE = "aws_networkmanager_site"
    AWS_NETWORKMANAGER_SITES = "aws_networkmanager_sites"

    # OpenSearch
    AWS_OPENSEARCH_DOMAIN = "aws_opensearch_domain"

    # OpsWorks

    # Organizations
    AWS_ORGANIZATIONS_DELEGATED_ADMINISTRATORS = "aws_organizations_delegated_administrators"
    AWS_ORGANIZATIONS_DELEGATED_SERVICES = "aws_organizations_delegated_services"
    AWS_ORGANIZATIONS_ORGANIZATION = "aws_organizations_organization"
    AWS_ORGANIZATIONS_ORGANIZATIONAL_UNITS = "aws_organizations_organizational_units"
    AWS_ORGANIZATIONS_RESOURCE_TAGS = "aws_organizations_resource_tags"

    # Outposts
    AWS_OUTPOSTS_ASSET = "aws_outposts_asset"
    AWS_OUTPOSTS_ASSETS = "aws_outposts_assets"
    AWS_OUTPOSTS_OUTPOST = "aws_outposts_outpost"
    AWS_OUTPOSTS_OUTPOST_INSTANCE_TYPE = "aws_outposts_outpost_instance_type"
    AWS_OUTPOSTS_OUTPOST_INSTANCE_TYPES = "aws_outposts_outpost_instance_types"
    AWS_OUTPOSTS_OUTPOSTS = "aws_outposts_outposts"
    AWS_OUTPOSTS_SITE = "aws_outposts_site"
    AWS_OUTPOSTS_SITES = "aws_outposts_sites"

    # Outposts (EC2)
    AWS_EC2_COIP_POOL = "aws_ec2_coip_pool"
    AWS_EC2_COIP_POOLS = "aws_ec2_coip_pools"
    AWS_EC2_LOCAL_GATEWAY = "aws_ec2_local_gateway"
    AWS_EC2_LOCAL_GATEWAY_ROUTE_TABLE = "aws_ec2_local_gateway_route_table"
    AWS_EC2_LOCAL_GATEWAY_ROUTE_TABLES = "aws_ec2_local_gateway_route_tables"
    AWS_EC2_LOCAL_GATEWAY_VIRTUAL_INTERFACE = "aws_ec2_local_gateway_virtual_interface"
    AWS_EC2_LOCAL_GATEWAY_VIRTUAL_INTERFACE_GROUP = "aws_ec2_local_gateway_virtual_interface_group"
    AWS_EC2_LOCAL_GATEWAY_VIRTUAL_INTERFACE_GROUPS = "aws_ec2_local_gateway_virtual_interface_groups"
    AWS_EC2_LOCAL_GATEWAYS = "aws_ec2_local_gateways"

    # Pinpoint
    AWS_PRICING_PRODUCT = "aws_pricing_product"

    # QLDB (Quantum Ledger Database)
    AWS_QLDB_LEDGER = "aws_qldb_ledger"

    # QuickSight

    # RAM (Resource Access Manager)
    AWS_RAM_RESOURCE_SHARE = "aws_ram_resource_share"

    # RDS (Relational Database)
    AWS_DB_CLUSTER_SNAPSHOT = "aws_db_cluster_snapshot"
    AWS_DB_EVENT_CATEGORIES = "aws_db_event_categories"
    AWS_DB_INSTANCE = "aws_db_instance"
    AWS_DB_PROXY = "aws_db_proxy"
    AWS_DB_SNAPSHOT = "aws_db_snapshot"
    AWS_DB_SUBNET_GROUP = "aws_db_subnet_group"
    AWS_RDS_CERTIFICATE = "aws_rds_certificate"
    AWS_RDS_CLUSTER = "aws_rds_cluster"
    AWS_RDS_ENGINE_VERSION = "aws_rds_engine_version"
    AWS_RDS_ORDERABLE_DB_INSTANCE = "aws_rds_orderable_db_instance"
    AWS_RDS_RESERVED_INSTANCE_OFFERING = "aws_rds_reserved_instance_offering"

    # Redshift
    AWS_REDSHIFT_CLUSTER = "aws_redshift_cluster"
    AWS_REDSHIFT_CLUSTER_CREDENTIALS = "aws_redshift_cluster_credentials"
    AWS_REDSHIFT_ORDERABLE_CLUSTER = "aws_redshift_orderable_cluster"
    AWS_REDSHIFT_SERVICE_ACCOUNT = "aws_redshift_service_account"
    AWS_REDSHIFT_SUBNET_GROUP = "aws_redshift_subnet_group"

    # Redshift Data

    # Resource Groups Tagging
    AWS_RESOURCEGROUPSTAGGINGAPI_RESOURCES = "aws_resourcegroupstaggingapi_resources"

    # Roles Anywhere

    # Route 53
    AWS_ROUTE53_DELEGATION_SET = "aws_route53_delegation_set"
    AWS_ROUTE53_TRAFFIC_POLICY_DOCUMENT = "aws_route53_traffic_policy_document"
    AWS_ROUTE53_ZONE = "aws_route53_zone"

    # Route 53 Recovery Control Config

    # Route 53 Recovery Readiness
    AWS_ROUTE53_RESOLVER_ENDPOINT = "aws_route53_resolver_endpoint"
    AWS_ROUTE53_RESOLVER_FIREWALL_CONFIG = "aws_route53_resolver_firewall_config"
    AWS_ROUTE53_RESOLVER_FIREWALL_DOMAIN_LIST = "aws_route53_resolver_firewall_domain_list"
    AWS_ROUTE53_RESOLVER_FIREWALL_RULE_GROUP = "aws_route53_resolver_firewall_rule_group"
    AWS_ROUTE53_RESOLVER_FIREWALL_RULE_GROUP_ASSOCIATION = "aws_route53_resolver_firewall_rule_group_association"
    AWS_ROUTE53_RESOLVER_FIREWALL_RULES = "aws_route53_resolver_firewall_rules"
    AWS_ROUTE53_RESOLVER_RULE = "aws_route53_resolver_rule"
    AWS_ROUTE53_RESOLVER_RULES = "aws_route53_resolver_rules"
    AWS_CANONICAL_USER_ID = "aws_canonical_user_id"
    AWS_S3_BUCKET = "aws_s3_bucket"
    AWS_S3_BUCKET_OBJECT = "aws_s3_bucket_object"
    AWS_S3_BUCKET_OBJECTS = "aws_s3_bucket_objects"
    AWS_S3_BUCKET_POLICY = "aws_s3_bucket_policy"
    AWS_S3_OBJECT = "aws_s3_object"
    AWS_S3_OBJECTS = "aws_s3_objects"

    # S3 Control
    AWS_S3_ACCOUNT_PUBLIC_ACCESS_BLOCK = "aws_s3_account_public_access_block"

    # S3 Glacier

    # S3 on Outposts

    # SDB (SimpleDB)
    AWS_SES_ACTIVE_RECEIPT_RULE_SET = "aws_ses_active_receipt_rule_set"
    AWS_SES_DOMAIN_IDENTITY = "aws_ses_domain_identity"
    AWS_SES_EMAIL_IDENTITY = "aws_ses_email_identity"

    # SESv2 (Simple Email V2)
    AWS_SESV2_DEDICATED_IP_POOL = "aws_sesv2_dedicated_ip_pool"
    AWS_SFN_ACTIVITY = "aws_sfn_activity"
    AWS_SFN_STATE_MACHINE = "aws_sfn_state_machine"

    # SNS (Simple Notification)
    AWS_SNS_TOPIC = "aws_sns_topic"
    AWS_SQS_QUEUE = "aws_sqs_queue"

    # SSM (Systems Manager)
    AWS_SSM_DOCUMENT = "aws_ssm_document"
    AWS_SSM_INSTANCES = "aws_ssm_instances"
    AWS_SSM_MAINTENANCE_WINDOWS = "aws_ssm_maintenance_windows"
    AWS_SSM_PARAMETER = "aws_ssm_parameter"
    AWS_SSM_PARAMETERS_BY_PATH = "aws_ssm_parameters_by_path"
    AWS_SSM_PATCH_BASELINE = "aws_ssm_patch_baseline"

    # SSO Admin
    AWS_SSOADMIN_INSTANCES = "aws_ssoadmin_instances"
    AWS_SSOADMIN_PERMISSION_SET = "aws_ssoadmin_permission_set"
    AWS_IDENTITYSTORE_GROUP = "aws_identitystore_group"
    AWS_IDENTITYSTORE_USER = "aws_identitystore_user"
    AWS_CALLER_IDENTITY = "aws_caller_identity"

    # SWF (Simple Workflow)

    # SageMaker
    AWS_SAGEMAKER_PREBUILT_ECR_IMAGE = "aws_sagemaker_prebuilt_ecr_image"
    AWS_SECRETSMANAGER_RANDOM_PASSWORD = "aws_secretsmanager_random_password"
    AWS_SECRETSMANAGER_SECRET = "aws_secretsmanager_secret"
    AWS_SECRETSMANAGER_SECRET_ROTATION = "aws_secretsmanager_secret_rotation"
    AWS_SECRETSMANAGER_SECRET_VERSION = "aws_secretsmanager_secret_version"
    AWS_SECRETSMANAGER_SECRETS = "aws_secretsmanager_secrets"

    # Security Hub

    # Serverless Application Repository
    AWS_SERVERLESSAPPLICATIONREPOSITORY_APPLICATION = "aws_serverlessapplicationrepository_application"
    AWS_SERVICECATALOG_CONSTRAINT = "aws_servicecatalog_constraint"
    AWS_SERVICECATALOG_LAUNCH_PATHS = "aws_servicecatalog_launch_paths"
    AWS_SERVICECATALOG_PORTFOLIO = "aws_servicecatalog_portfolio"
    AWS_SERVICECATALOG_PORTFOLIO_CONSTRAINTS = "aws_servicecatalog_portfolio_constraints"
    AWS_SERVICECATALOG_PRODUCT = "aws_servicecatalog_product"

    # Service Quotas
    AWS_SERVICEQUOTAS_SERVICE = "aws_servicequotas_service"
    AWS_SERVICEQUOTAS_SERVICE_QUOTA = "aws_servicequotas_service_quota"

    # Shield

    # Signer
    AWS_SIGNER_SIGNING_JOB = "aws_signer_signing_job"
    AWS_SIGNER_SIGNING_PROFILE = "aws_signer_signing_profile"
    AWS_STORAGEGATEWAY_LOCAL_DISK = "aws_storagegateway_local_disk"

    # Transcribe
    AWS_TRANSFER_SERVER = "aws_transfer_server"
    AWS_EC2_TRANSIT_GATEWAY = "aws_ec2_transit_gateway"
    AWS_EC2_TRANSIT_GATEWAY_ATTACHMENT = "aws_ec2_transit_gateway_attachment"
    AWS_EC2_TRANSIT_GATEWAY_CONNECT = "aws_ec2_transit_gateway_connect"
    AWS_EC2_TRANSIT_GATEWAY_CONNECT_PEER = "aws_ec2_transit_gateway_connect_peer"
    AWS_EC2_TRANSIT_GATEWAY_DX_GATEWAY_ATTACHMENT = "aws_ec2_transit_gateway_dx_gateway_attachment"
    AWS_EC2_TRANSIT_GATEWAY_MULTICAST_DOMAIN = "aws_ec2_transit_gateway_multicast_domain"
    AWS_EC2_TRANSIT_GATEWAY_PEERING_ATTACHMENT = "aws_ec2_transit_gateway_peering_attachment"
    AWS_EC2_TRANSIT_GATEWAY_ROUTE_TABLE = "aws_ec2_transit_gateway_route_table"
    AWS_EC2_TRANSIT_GATEWAY_ROUTE_TABLES = "aws_ec2_transit_gateway_route_tables"
    AWS_EC2_TRANSIT_GATEWAY_VPC_ATTACHMENT = "aws_ec2_transit_gateway_vpc_attachment"
    AWS_EC2_TRANSIT_GATEWAY_VPC_ATTACHMENTS = "aws_ec2_transit_gateway_vpc_attachments"
    AWS_EC2_TRANSIT_GATEWAY_VPN_ATTACHMENT = "aws_ec2_transit_gateway_vpn_attachment"

    # VPC (Virtual Private Cloud)
    AWS_EC2_MANAGED_PREFIX_LIST = "aws_ec2_managed_prefix_list"
    AWS_EC2_MANAGED_PREFIX_LISTS = "aws_ec2_managed_prefix_lists"
    AWS_EC2_NETWORK_INSIGHTS_ANALYSIS = "aws_ec2_network_insights_analysis"
    AWS_EC2_NETWORK_INSIGHTS_PATH = "aws_ec2_network_insights_path"
    AWS_INTERNET_GATEWAY = "aws_internet_gateway"
    AWS_NAT_GATEWAY = "aws_nat_gateway"
    AWS_NAT_GATEWAYS = "aws_nat_gateways"
    AWS_NETWORK_ACLS = "aws_network_acls"
    AWS_NETWORK_INTERFACE = "aws_network_interface"
    AWS_NETWORK_INTERFACES = "aws_network_interfaces"
    AWS_PREFIX_LIST = "aws_prefix_list"
    AWS_ROUTE = "aws_route"
    AWS_ROUTE_TABLE = "aws_route_table"
    AWS_ROUTE_TABLES = "aws_route_tables"
    AWS_SECURITY_GROUP = "aws_security_group"
    AWS_SECURITY_GROUPS = "aws_security_groups"
    AWS_SUBNET = "aws_subnet"
    AWS_SUBNET_IDS = "aws_subnet_ids"
    AWS_SUBNETS = "aws_subnets"
    AWS_VPC = "aws_vpc"
    AWS_VPC_DHCP_OPTIONS = "aws_vpc_dhcp_options"
    AWS_VPC_ENDPOINT = "aws_vpc_endpoint"
    AWS_VPC_ENDPOINT_SERVICE = "aws_vpc_endpoint_service"
    AWS_VPC_PEERING_CONNECTION = "aws_vpc_peering_connection"
    AWS_VPC_PEERING_CONNECTIONS = "aws_vpc_peering_connections"
    AWS_VPCS = "aws_vpcs"

    # VPC IPAM (IP Address Manager)
    AWS_VPC_IPAM_POOL = "aws_vpc_ipam_pool"
    AWS_VPC_IPAM_POOL_CIDRS = "aws_vpc_ipam_pool_cidrs"
    AWS_VPC_IPAM_POOLS = "aws_vpc_ipam_pools"
    AWS_VPC_IPAM_PREVIEW_NEXT_CIDR = "aws_vpc_ipam_preview_next_cidr"

    # VPN (Client)
    AWS_EC2_CLIENT_VPN_ENDPOINT = "aws_ec2_client_vpn_endpoint"
    AWS_CUSTOMER_GATEWAY = "aws_customer_gateway"
    AWS_VPN_GATEWAY = "aws_vpn_gateway"

    # WAF
    AWS_WAFV2_IP_SET = "aws_wafv2_ip_set"
    AWS_WAFV2_REGEX_PATTERN_SET = "aws_wafv2_regex_pattern_set"
    AWS_WAFV2_RULE_GROUP = "aws_wafv2_rule_group"
    AWS_WAFV2_WEB_ACL = "aws_wafv2_web_acl"

    # WAF Classic
    AWS_WAF_IPSET = "aws_waf_ipset"
    AWS_WAF_RATE_BASED_RULE = "aws_waf_rate_based_rule"
    AWS_WAF_RULE = "aws_waf_rule"
    AWS_WAF_SUBSCRIBED_RULE_GROUP = "aws_waf_subscribed_rule_group"
    AWS_WAF_WEB_ACL = "aws_waf_web_acl"
    AWS_WAFREGIONAL_IPSET = "aws_wafregional_ipset"
    AWS_WAFREGIONAL_RATE_BASED_RULE = "aws_wafregional_rate_based_rule"
    AWS_WAFREGIONAL_RULE = "aws_wafregional_rule"
    AWS_WAFREGIONAL_SUBSCRIBED_RULE_GROUP = "aws_wafregional_subscribed_rule_group"
    AWS_WAFREGIONAL_WEB_ACL = "aws_wafregional_web_acl"

    # Wavelength

    # WorkLink

    # WorkSpaces
    AWS_WORKSPACES_BUNDLE = "aws_workspaces_bundle"
    AWS_WORKSPACES_DIRECTORY = "aws_workspaces_directory"
    AWS_WORKSPACES_IMAGE = "aws_workspaces_image"
    AWS_WORKSPACES_WORKSPACE = "aws_workspaces_workspace"


    # X-Ray

