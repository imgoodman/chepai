<?php
header("Access-Control-Allow-Origin:*");
header("Content-Type:application/json;charset=UTF-8");
// echo urldecode($_SERVER["QUERY_STRING"]);
$req=urldecode($_SERVER["QUERY_STRING"]);
// echo $req;
$params=array(
    "p"=>0,
    "pSize"=>10,
    "name"=>"",
    "applier_name"=>"",
    "inventor_name"=>"",
    "publish_date"=>"",
    "orderBy"=>"name",
    "orderType"=>"asc"
);
$paramArray=split("&",$req);
foreach($paramArray as $p){
    $pArr=split("=",$p);
    $params[$pArr[0]]=$pArr[1];
}
$link=mysql_connect("********","********","********");

if(!$link){
    echo "fail";
}
$result=array();
$items=array();
mysql_select_db("qdm115145384_db",$link);
mysql_set_charset("utf8",$link);
$sql_cnt="select count(0) from t_patent where state=1 ";
$sql="select id,name,publish_date,applier_name,inventor_name from t_patent where state=1 ";
if($params["name"]!=""){
    $sql.=" and name like '%".$params["name"]."%'";
    $sql_cnt.=" and name like '%".$params["name"]."%'";
}
if($params["applier_name"]!=""){
    $sql.=" and applier_name like '%".$params["applier_name"]."%'";
    $sql_cnt.=" and name like '%".$params["name"]."%'";
}
if($params["inventor_name"]!=""){
    $sql.=" and inventor_name like '%".$params["inventor_name"]."%'";
    $sql_cnt.=" and name like '%".$params["name"]."%'";
}
if($params["publish_date"]!=""){
    $sql.=" and publish_date='".$params["publish_date"]."'";
    $sql_cnt.=" and name like '%".$params["name"]."%'";
}
$cnt=mysql_query($sql_cnt,$link);
// echo mysql_fetch_array($cnt)["0"];
foreach(mysql_fetch_array($cnt) as $key=>$value)
{
    // echo $key;
    // echo $value;
    $result["total"]=$value;
}
// $result["total"]=mysql_fetch_array($cnt)[0];
$sql.=" order by ".$params["orderBy"]." ".$params["orderType"]." limit ".$params["p"]*$params["pSize"].",".$params["pSize"];
// echo $sql;
$rs=mysql_query($sql,$link);
while($row=mysql_fetch_object($rs)){
    $item=array();
    foreach($row as $key=>$value){
        $item[$key]=urlencode($value);
    }
    array_push($items,$item);
}
$result["rows"]=$items;
echo urldecode(json_encode($result));
mysql_close($link);
?>