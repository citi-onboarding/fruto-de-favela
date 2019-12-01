$('#formContato').submit(function(e) {
    e.preventDefault();
    const nome = $('input[name=nome]').val();
    const email = $('input[name=email]').val();
    const assunto = $('input[name=assunto]').val();
    const mensagem = $('input[name=mensagem]').val();

    const token = jQuery('[name=csrfmiddlewaretoken]').val();

    $.ajax({
        type: 'POST',
        url: '/contato',
        data: {
        'csrfmiddlewaretoken': token,
        'nome': nome,
        'email': email,
        'assunto': assunto,
        'mensagem': mensagem
        },
        sucess: clear(),
    })
});


const form = document.querySelector('#formContato');
const name = form.querySelector('input[name=nome]');
const mail = form.querySelector('input[name=email]');
const subject = form.querySelector('input[name=assunto]');
const message = form.querySelector('textarea[name=mensagem]');

function clear() {
    name.value = '';
    mail.value = '';
    subject.value = '';
    message.value = '';
}