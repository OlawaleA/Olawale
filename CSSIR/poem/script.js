function DisplayPoem(info, info2, info3) {
    var poem = "Jack: Who makes all these? " + info +": "+ info2 + " I do, and I practice with them three " + info3;
    /* +" a day.Jack: You need to " + info[3] +" yourself a " + info[4] + ", mate. Or perhaps the reason you practice three " + info[5] + " a day is because you`ve already " + info[6] + " one, and are otherwise incapable of " + info[7] +
    " said strumpet. You`re not a " + info[8] +
    ", are you? " + info[9] + ": I practice three " + info[10] +
    " a day so that when I meet a " + info[11] + ", I can " + info[12] + " it! Jack: Ah.";*/
    $('#output').html(poem);
}

$('#submitName').click(function(){

    var passThis= $('input[name="studentName"]').val();
    var passThis2 = $('input[name="studentName2"]').val();
    var passThis3 = $('input[name="studentName3"]').val();
  /*  passThis[3]=  $('input[name="noun"]').val();
    passThis[4]=  $('input[name="noun"]').val();
    passThis[5]=  $('input[name="noun"]').val();
    passThis[6]=  $('input[name="noun"]').val();
    passThis[7]=  $('input[name="noun"]').val();
    passThis[8]=  $('input[name="noun"]').val();
    passThis[9]=  $('input[name="noun"]').val();
    passThis[10]=  $('input[name="noun"]').val();
    passThis[11]=  $('input[name="noun"]').val();
    passThis[12]=  $('input[name="noun"]').val();*/
    DisplayPoem(passThis, passThis2, passThis3);
});
