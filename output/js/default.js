$( function () {
    $('.datatable').DataTable({
      'paging': false,
      'language': {
          "url": "https://cdn.datatables.net/plug-ins/1.10.20/i18n/Dutch.json"
      },
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
        null,
        null,
        null
      ]
    });
});
