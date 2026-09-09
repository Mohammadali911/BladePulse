CREATE EXTERNAL TABLE IF NOT EXISTS bladepulse.assumption_registry (
    assumption_id string,
    category string,
    variable_name string,
    description string,
    unit string,
    baseline_value string,
    low_value string,
    high_value string,
    distribution string,
    evidence_class string,
    confidence_score string,
    source_url string,
    source_date string,
    scenario_scope string,
    research_status string,
    notes string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES ('separatorChar' = ',')
STORED AS TEXTFILE
LOCATION 's3://bladepulse-data-lake-datalakebucket-o8wa2tuz76ch/reference/assumptions/'
TBLPROPERTIES ('skip.header.line.count' = '1');