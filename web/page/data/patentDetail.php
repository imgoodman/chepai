<?php
header("Access-Control-Allow-Origin:*");
header("Content-Type:application/json;charset=UTF-8");
// echo urldecode($_SERVER["QUERY_STRING"]);
$req=urldecode($_SERVER["QUERY_STRING"]);
if(!$req){
    echo "no id";
}
// echo $req;
$params=array(
    "id"=>1
);
$paramArray=split("&",$req);
foreach($paramArray as $p){
    $pArr=split("=",$p);
    $params[$pArr[0]]=$pArr[1];
}
$link=mysql_connect("********.my3w.com","********","********");

if(!$link){
    echo "fail to connect db";
}
$result=array();
mysql_select_db("qdm115145384_db",$link);
mysql_set_charset("utf8",$link);
$sql="select name,apply_code,apply_date,publish_code,publish_date,ipc_code,applier_name,inventor_name,abstract,figure_id,baiten_image_url from t_patent where state=1 and id=".$params["id"];
// echo $sql;
$rs=mysql_query($sql);
$row=mysql_fetch_object($rs);
$item=array();
foreach($row as $key=>$value){
    $item[$key]=urlencode($value);
}
$result["detail"]=$item;
echo urldecode(json_encode($result));
mysql_close($link);
?>