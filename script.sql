
/*Data source: https://data.humdata.org/dataset/kutupalong-infrastructure-risk-to-flood-and-landslide-hazards */

DROP TABLE IF EXISTS camps;
CREATE TABLE camps (
  camps_FID text,
  camps_district text,
  camps_upazila text,
  camps_union text,
  camps_settlement text,
  camps_campname text,
  camps_coord_group text,
  camps_unique_id text,
  camps_facility_c text,
  camps_facility text,
  camps_geo_co text,
  camps_funding text,
  camps_implemen_part text,
  camps_landslide text, 
  camps_floods text, 
  camps_l_risk text, 
  camps_f_risk text, 
  camps_both_risk text, 
  camps_either_risk text,
  PRIMARY KEY(camps_FID)
  ) ;

.separator ","
.import refugeecamp.csv camps 
.mode columns 

DELETE FROM camps WHERE camps_FID = "FID";
