
<!-- НАЧАЛО модального окна -->
<link rel="stylesheet" href="style/modal.css" />
<div class="modal" data-modal="1">
   <!--   Svg иконка для закрытия окна  -->
   <svg class="modal__cross js-modal-close" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M23.954 21.03l-9.184-9.095 9.092-9.174-2.832-2.807-9.09 9.179-9.176-9.088-2.81 2.81 9.186 9.105-9.095 9.184 2.81 2.81 9.112-9.192 9.18 9.1z"/></svg>
   <p class="modal__title"><b>Отредактировать строку</b><br /></p>
   
<form action="index.py" method="get">   
   <input type="hidden" name="textId" id="textId" value="none 1 is error" />
   <br /><i>Параметр #1:</i> <input type="edit" name="textEd1" id="textEd1" value="none 1 is error" /><br />
   <br /><i>Параметр #2:</i> <input type="edit" name="textEd2" id="textEd2" value="none 2 is error" /><br />
   <br /><i>Параметр #3:</i> <input type="edit" name="textEd3" id="textEd3" value="none 3 is error" /><br />
<br /><!-- <a href="practUpload/index.php?id=error" id="aId" target="_blank" class="bt">Добавить файлы</a> -->
	<input type="submit" name="bt2" value="Отредактировать" class="bt" />
</form>
   
</div>
	<!-- Подложка под модальным окном -->
<div class="overlay js-overlay-modal"></div>
	<!-- Дополнительный скрипт --> 
<script src="script/modal1.js"></script>
<!-- КОНЕЦ модального окна -->
 
	</div>
	
	<link rel="stylesheet" href="scrollup/scrollup.css" /><div id="scrollup"><img src="scrollup/7.png" class="up" title="Прокрутить вверх" /></div><script src="scrollup/scrollup.js"></script>

</body>
</html>