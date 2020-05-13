<html>

<head>
    <meta charset='utf-8'>
    <title>HTML SCRAPING</title>
    <link href="styles.css" rel="stylesheet" type="text/css">    


    <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
    <link rel="stylesheet" href="/resources/demos/style.css">
    <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>   

    <script type="text/javascript">
     $( function() {
      $( "#datepicker" ).datepicker({
        dateFormat: "dd.mm.yy",
              showOn: "button",
      buttonImage: "calendar.png",
      buttonImageOnly: true,
      buttonText: "Select date"
     });
    } );

    </script> 
</head>

<body>
    <div id="navigation">
        <div id="banner">
            <img src="file:///home/ssj/Desktop/new_project/bilder/internet.svg" width="100px" height="100px">
            <h1>Datenbank</h1>
        </div>

        <p id="menu">
            <a href="index.html">HTML SCRAPING</a>
            <a href="ueber_uns.html">&Uuml;BER UNS </a>
            <a href="Teampage.html">UNSER PROJEKT </a>
            <a href="Datenbank.php">DATENBANK</a>
        </p>
    </div>


    <div id="inhalt">
     
    <form name="form" id="form" method="post" action="Datenbank.php">
      <p>Datum: <input name="use_date" type="text" id="datepicker" value="{$use_date}"></p> 
      <input type="submit" class="button" value="Suchen">&nbsp;
    </form>     

   {section name=index loop=$artikel.artikel_nr}

     <div class="database">
            <div class="database_column">
              <h3>
               <img src="getImage.php?id={$artikel.quelle_nr[index]}" height="50px"/> 
              </h3>
              <div class="database_item">
              <p>{$artikel.schlagzeile[index]}</p>    
              <p>{$artikel.artikeltext[index]}</p>
              <p>{$artikel.bezeichnung[index]} - Autor: {$artikel.nachname[index]}, {$artikel.vorname[index]} ({$artikel.alter[index]})</p>
            </div>
        </div>
    </div>
                
   {/section}  

    <div id="footer">
        <p> Copyright Â© Sezer,Sergej,Jonas </p>
    </div>

    <script src="main.js"></script>
</body>

</html>
