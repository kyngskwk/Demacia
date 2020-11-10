<template>
  <div>


  <v-container>
    <v-row justify="space-around">
      <v-card width="800" >
                <v-card-title class="black--text mt-2" >
            <v-avatar size="56">
              <img
                alt="user"
                src="https://cdn.pixabay.com/photo/2020/06/24/19/12/cabbage-5337431_1280.jpg"
              >
            </v-avatar>
            <p class="ml-3 mt-2">
              John Doe
            </p>
                        <p class="ml-10 mt-2">
              EVENT TIMELINE
            </p>
          </v-card-title>
       <video
        style="width: 100%; padding: 0; max-width: 900px"
        controls
        autoplay="true"
        name="media"
        id="vid"
      >
        
       
          <v-app-bar
            flat
            color="rgba(0, 0, 0, 0)"
          >
            <v-app-bar-nav-icon color="white"></v-app-bar-nav-icon>

            <v-toolbar-title class="title white--text pl-0">
              Messages
            </v-toolbar-title>

            <v-spacer></v-spacer>

            <v-btn
              color="white"
              icon
            >
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </v-app-bar>


        <source src="./4659518008_01.mp4" type="video/mp4" />
      </video>

        <v-card-text>
          <div class="font-weight-bold ml-8 mb-2">
            TIME LINE
          </div>

          <v-timeline
            align-top
            dense
          >
            <v-timeline-item
              v-for="message in messages"
              :key="message.time"
              :color="message.color"
              small
            >
              <div>
                <div class="font-weight-normal">
                  <strong>{{ message.from }}</strong> @{{ message.time }}
                </div>
                <div>{{ message.message }}</div>
              </div>
            </v-timeline-item>
          </v-timeline>
        </v-card-text>
      </v-card>
    </v-row>
  </v-container>

  </div>
</template>

<script>
export default {
    name: "VideoDetail1",
    data: () => ({
      messages: [
        { time: '15:43', from:"샤코", color:"#3F51B5",  message: "대지 드래곤 KILL" },
        { time: '15:45', from:"노틸러스", color:"#F44336",  message: "스웨인 KILL" },
        { time: '15:54', from:"노틸러스", color:"#F44336",  message: "샤코 KILL" },
        { time: '16:02', from:"아리", color:"#3F51B5",  message: "헤카림 KILL" },
        { time: '16:05', from:"아리", color:"#3F51B5",  message: "노틸러스 KILL" },

      ],
    }),  
}
</script>

<style>

</style>