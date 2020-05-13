<?php

 // config einlesen
 include 'config.inc.php';
 
 // Template starten
 require_once('smarty/libs/Smarty.class.php');
 $smarty = new Smarty;
 $smarty->template_dir =   "smartyfiles/templates/";
 $smarty->config_dir   =   "smartyfiles/config/";
 $smarty->compile_dir  =   "smartyfiles/templates_c/";
 $smarty->cache_dir    =   "smartyfiles/cache/";

 // Datenbankverbindung herstellen
 $mysqli = new mysqli($server, $db_user, $pw, $db)
   or die ("Failed to connect to MySQL: (".$mysqli->connect_errno.")".$mysqli->connect_error);


// Datum holen 
if (!isset($_REQUEST['use_date']))
{
   $timestamp = time();
   $use_date = date("d.m.Y", $timestamp); 
   $sql_date = date_create($use_date)->format('Y-m-d');   
} 
else
{
   $use_date = $_REQUEST['use_date'];  
   $sql_date = date_create($use_date)->format('Y-m-d');   
}    

 
 $SQLStr = "SELECT 
             artikel.artikel_nr,
             artikel.schlagzeile,
             artikel.artikeltext,
             artikel.kicker,
             autor.vorname,
             autor.nachname,
             autor.alter,
             quelle.quelle_nr,
             quelle.bezeichnung,
             quelle.adresse,
             quelle.logo
             
            FROM artikel, autor, quelle 
            WHERE 
            artikel.autor_nr = autor.autor_nr AND
            artikel.quelle_nr = quelle.quelle_nr AND
            artikel.einstelldatum='$sql_date' order by quelle.quelle_nr"; 
 
 //echo "$SQLStr";
 $result = $mysqli->query($SQLStr)
    or die ("SQL - Error:".$this->mysqli->error);

 //$row=$result->fetch_array(MYSQLI_NUM)
while($row = $result->fetch_assoc())
{
  $artikel['artikel_nr'][]    = $row['artikel_nr'];
  $artikel['schlagzeile'][]   = $row['schlagzeile'];
  $artikel['artikeltext'][]   = $row['artikeltext'];
  $artikel['kicker'][]        = $row['kicker'];
  $artikel['vorname'][]       = $row['vorname'];
  $artikel['nachname'][]      = $row['nachname'];
  $artikel['alter'][]         = $row['alter'];
  $artikel['bezeichnung'][]   = $row['bezeichnung'];
  $artikel['adresse'][]       = $row['adresse'];
  $artikel['quelle_nr'][]     = $row['quelle_nr'];
} 
  
$smarty->assign("use_date",$use_date);  
$smarty->assign("artikel",$artikel);  
$smarty->display('db.tpl');  



