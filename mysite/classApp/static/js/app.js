  

var app1 = new Vue({
  el: '#app-1',
  data: {
    customers: [],
    seen:true,
    unseen:false
  },

  created: function() {
    this.fetchChartData();
    this.timer = setInterval(this.fetchChartData,60000);
  },
  methods: {
    fetchChartData: function() {
      axios
        .get('/Data_Visualization/')
        .then(response => (this.customers = response.data.customers))
        console.log(this.customers)
    },
    cancelAutoUpdate: function() {clearInterval(this.timer)}
  },
  beforeDestroy() {
    this.cancelAutoUpdate();
  }
})


  // var app4 = new Vue({
  //   el: '#app-4',
  //   data: {
  //       story: [],
  //       seen:true,
  //       unseen:false
  //     },
  //     //Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
  //     created: function() {
  //           this.fetchStoryList();
  //           this.timer = setInterval(this.fetchStoryList, 60000);
  //     },
  //     methods: {
  //       fetchStoryList: function() {
  //           // $.get('/suggestions/', function(suggest_list) {
  //           //     this.suggestions = suggest_list.suggestions;
  //           //     console.log(suggest_list);
  //           // }.bind(this));
  //           axios
  //             .get('/test/')
  //             // .then(response => console.log(response.data))
  //             .then(response => (this.story = response.data.story))
  //           console.log(this.story)
  //           this.seen=false
  //           this.unseen=true
  //       },
  //       cancelAutoUpdate: function() { clearInterval(this.timer) }
  //     },
  //     beforeDestroy() {
  //       // clearInterval(this.timer)
  //       this.cancelAutoUpdate();
  //     }
  // })