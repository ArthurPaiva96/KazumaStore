/// <reference path="../../typings/globals/jquery/index.d.ts" />

$(function () {
  // $('[data-toggle="tooltip"]').tooltip();
  // $('[data-toggle="popover"]').popover();

  var iconeDislikeEmpty = "far fa-thumbs-down";
  var iconeDislikeFull = "fas fa-thumbs-down";

  var iconeLikeEmpty = "far fa-thumbs-up";
  var iconeLikeFull = "fas fa-thumbs-up"

  function dislikeCheio(iconeDislike) {

    $(iconeDislike).removeClass(iconeDislikeEmpty);
    $(iconeDislike).addClass(iconeDislikeFull);
  }

  function dislikeVazio(iconeDislike) {

    $(iconeDislike).removeClass(iconeDislikeFull);
    $(iconeDislike).addClass(iconeDislikeEmpty);
  }

  function likeCheio(iconeLike) {
    
    $(iconeLike).removeClass(iconeLikeEmpty);
    $(iconeLike).addClass(iconeLikeFull);
  }

  function likeVazio(iconeLike) {

    $(iconeLike).removeClass(iconeLikeFull);
    $(iconeLike).addClass(iconeLikeEmpty);
  }

  $("#likesKonoSubaDVD").click(function () {

    var botaoDislike = $("#dislikesKonoSubaDVD");


    if ($(this).hasClass(iconeLikeEmpty)) {

      if (botaoDislike.hasClass(iconeDislikeFull)) {

        dislikeVazio(botaoDislike);
        likeCheio($(this));
        $("#numeroDislikesKonoSubaDVD").text(botaoDislike.data("dislike"));
        
      }else{
        likeCheio($(this));
      }

      $("#numeroLikesKonoSubaDVD").text($(this).data("like")+1);

    } else if ($(this).hasClass(iconeLikeFull)) {
            
      likeVazio($(this));
      $("#numeroLikesKonoSubaDVD").text($(this).data("like"));
    }

  });

  $("#dislikesKonoSubaDVD").click(function () {

    var botaoLike = $("#likesKonoSubaDVD");

    if ($(this).hasClass(iconeDislikeEmpty)) {

      if(botaoLike.hasClass(iconeLikeFull)){
        
        likeVazio(botaoLike);
        dislikeCheio($(this));
        $("#numeroLikesKonoSubaDVD").text(botaoLike.data("like"));

      }else{
        dislikeCheio($(this));
      }

      $("#numeroDislikesKonoSubaDVD").text($(this).data("dislike")+1);

    } else if ($(this).hasClass(iconeDislikeFull)) {

      dislikeVazio($(this));
      $("#numeroDislikesKonoSubaDVD").text($(this).data("dislike"));
    }

  });





  $("#botaoCadastrarNovoProduto").click(function () {
    if ($("#adicionaProdutoNome").val().length > 0 &&
      $("#adicionaDescricao").val().length > 0 &&
      $("[name=opcaoTipoProduto]").is(":checked") &&
      $("[name=opcaoIdiomaProduto]").is(":checked") &&
      $("#comboboxObra").val().length > 0 &&
      $("#precoProdutoCadastrado").val() > 0) {

      var idiomas = '';
      var tipo;

      $("input[name=opcaoTipoProduto]:checked").each(function () {
        var idTipo = $(this).attr("id");
        tipo = $("label[for=\"" + idTipo + "\"]").text();
      });
      $("input[name=opcaoIdiomaProduto]:checked").each(function () {
        var idIdioma = $(this).attr("id");
        idiomas += " " + $("label[for=\"" + idIdioma + "\"]").text();
      });


      $("#rowProdutos").prepend('<div class="col-12 mb-3"><div class="card text-center ' + tipo.toLowerCase() + '"><h5 class="card-header">' + $("#adicionaProdutoNome").val() + '</h5><div class="card-body"><p class="card-text mb-4">' + $("#adicionaDescricao").val() + '<div>Idiomas: ' + idiomas + '</div><br><div>Anime: ' + $("#comboboxObra").val() + '</div></div></p><h3 class="text-center">R$' + $("#precoProdutoCadastrado").val().toString().replace(".", ",") + '</h3><div class="text-right"><a href="#" class="btn btn-primary" style="float: right;">Comprar</a><input class="form-control mr-2" type="number" style="width: 70px; float:right;"></div></div></div>');

    } else {
      window.alert("Fail");
    }
  });




})