$(document).ready( function () {
    $('.datatable').DataTable({
      'paging': false,
      'buttons': {
        'dom': {
          'button': {
            'className': 'btn'
          }
        }
      },
      'columns': [
        { 'searchable': false },
        null,
        null
      ]
    });
});
