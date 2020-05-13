<?php
/* Smarty version 3.1.33, created on 2020-05-11 11:09:47
  from 'E:\xampp2020\htdocs\html_scrapping\smartyfiles\templates\db.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5eb9165b55b2d7_77252819',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'd2810add91a018980771cb9c7548f5dfd8d020e2' => 
    array (
      0 => 'E:\\xampp2020\\htdocs\\html_scrapping\\smartyfiles\\templates\\db.tpl',
      1 => 1589188183,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5eb9165b55b2d7_77252819 (Smarty_Internal_Template $_smarty_tpl) {
?><html>

<head>
    <meta charset='utf-8'>
    <title>HTML SCRAPING</title>
    <link href="styles.css" rel="stylesheet" type="text/css">    


    <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
    <link rel="stylesheet" href="/resources/demos/style.css">
    <?php echo '<script'; ?>
 src="https://code.jquery.com/jquery-1.12.4.js"><?php echo '</script'; ?>
>
    <?php echo '<script'; ?>
 src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"><?php echo '</script'; ?>
>   

    <?php echo '<script'; ?>
 type="text/javascript">
     $( function() {
      $( "#datepicker" ).datepicker({
        dateFormat: "dd.mm.yy",
              showOn: "button",
      buttonImage: "calendar.png",
      buttonImageOnly: true,
      buttonText: "Select date"
     });
    } );

    <?php echo '</script'; ?>
> 
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
      <p>Datum: <input name="use_date" type="text" id="datepicker" value="<?php echo $_smarty_tpl->tpl_vars['use_date']->value;?>
"></p> 
      <input type="submit" class="button" value="Suchen">&nbsp;
    </form>     

   <?php
$__section_index_0_loop = (is_array(@$_loop=$_smarty_tpl->tpl_vars['artikel']->value['artikel_nr']) ? count($_loop) : max(0, (int) $_loop));
$__section_index_0_total = $__section_index_0_loop;
$_smarty_tpl->tpl_vars['__smarty_section_index'] = new Smarty_Variable(array());
if ($__section_index_0_total !== 0) {
for ($__section_index_0_iteration = 1, $_smarty_tpl->tpl_vars['__smarty_section_index']->value['index'] = 0; $__section_index_0_iteration <= $__section_index_0_total; $__section_index_0_iteration++, $_smarty_tpl->tpl_vars['__smarty_section_index']->value['index']++){
?>

     <div class="database">
            <div class="database_column">
              <h3>
               <img src="getImage.php?id=<?php echo $_smarty_tpl->tpl_vars['artikel']->value['quelle_nr'][(isset($_smarty_tpl->tpl_vars['__smarty_section_index']->value['index']) ? $_smarty_tpl->tpl_vars['__smarty_section_index']->value['index'] : null)];?>
" height="50px"/> 
              </h3>
              <div class="database_item">
              <p><?php echo $_smarty_tpl->tpl_vars['artikel']->value['schlagzeile'][(isset($_smarty_tpl->tpl_vars['__smarty_section_index']->value['index']) ? $_smarty_tpl->tpl_vars['__smarty_section_index']->value['index'] : null)];?>
</p>    
              <p><?php echo $_smarty_tpl->tpl_vars['artikel']->value['artikeltext'][(isset($_smarty_tpl->tpl_vars['__smarty_section_index']->value['index']) ? $_smarty_tpl->tpl_vars['__smarty_section_index']->value['index'] : null)];?>
</p>
              <p><?php echo $_smarty_tpl->tpl_vars['artikel']->value['bezeichnung'][(isset($_smarty_tpl->tpl_vars['__smarty_section_index']->value['index']) ? $_smarty_tpl->tpl_vars['__smarty_section_index']->value['index'] : null)];?>
 - Autor: <?php echo $_smarty_tpl->tpl_vars['artikel']->value['nachname'][(isset($_smarty_tpl->tpl_vars['__smarty_section_index']->value['index']) ? $_smarty_tpl->tpl_vars['__smarty_section_index']->value['index'] : null)];?>
, <?php echo $_smarty_tpl->tpl_vars['artikel']->value['vorname'][(isset($_smarty_tpl->tpl_vars['__smarty_section_index']->value['index']) ? $_smarty_tpl->tpl_vars['__smarty_section_index']->value['index'] : null)];?>
 (<?php echo $_smarty_tpl->tpl_vars['artikel']->value['alter'][(isset($_smarty_tpl->tpl_vars['__smarty_section_index']->value['index']) ? $_smarty_tpl->tpl_vars['__smarty_section_index']->value['index'] : null)];?>
)</p>
            </div>
        </div>
    </div>
                
   <?php
}
}
?>  

    <div id="footer">
        <p> Copyright Â© Sezer,Sergej,Jonas </p>
    </div>

    <?php echo '<script'; ?>
 src="main.js"><?php echo '</script'; ?>
>
</body>

</html>
<?php }
}
