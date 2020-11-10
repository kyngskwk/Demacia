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
    <v-tabs vertical>
      <v-tab class="pl-0">
        <v-icon left>
          mdi-account
        </v-icon>
        TIME LINE
      </v-tab>
      <v-tab >
        <v-icon left>
          mdi-lock
        </v-icon>
        Champions
      </v-tab>
      <v-tab class="pl-2">
        <v-icon left>
          mdi-access-point
        </v-icon>
        Snapshot
      </v-tab>

      <v-tab-item>
        <v-card flat>
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
      </v-tab-item>
      <v-tab-item>
        <v-card flat>
          <v-card-text>
            <p>
              Morbi nec metus. Suspendisse faucibus, nunc et pellentesque egestas, lacus ante convallis tellus, vitae iaculis lacus elit id tortor. Sed mollis, eros et ultrices tempus, mauris ipsum aliquam libero, non adipiscing dolor urna a orci. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Nunc sed turpis.
            </p>

            <p>
              Suspendisse feugiat. Suspendisse faucibus, nunc et pellentesque egestas, lacus ante convallis tellus, vitae iaculis lacus elit id tortor. Proin viverra, ligula sit amet ultrices semper, ligula arcu tristique sapien, a accumsan nisi mauris ac eros. In hac habitasse platea dictumst. Fusce ac felis sit amet ligula pharetra condimentum.
            </p>

            <p>
              Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Nam commodo suscipit quam. In consectetuer turpis ut velit. Sed cursus turpis vitae tortor. Aliquam eu nunc.
            </p>

            <p>
              Etiam ut purus mattis mauris sodales aliquam. Ut varius tincidunt libero. Aenean viverra rhoncus pede. Duis leo. Fusce fermentum odio nec arcu.
            </p>

            <p class="mb-0">
              Donec venenatis vulputate lorem. Aenean viverra rhoncus pede. In dui magna, posuere eget, vestibulum et, tempor auctor, justo. Fusce commodo aliquam arcu. Suspendisse enim turpis, dictum sed, iaculis a, condimentum nec, nisi.
            </p>
          </v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card flat>
          <v-card-text>
            <p>
              Fusce a quam. Phasellus nec sem in justo pellentesque facilisis. Nam eget dui. Proin viverra, ligula sit amet ultrices semper, ligula arcu tristique sapien, a accumsan nisi mauris ac eros. In dui magna, posuere eget, vestibulum et, tempor auctor, justo.
            </p>

            <p class="mb-0">
              Cras sagittis. Phasellus nec sem in justo pellentesque facilisis. Proin sapien ipsum, porta a, auctor quis, euismod ut, mi. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nam at tortor in tellus interdum sagittis.
            </p>
          </v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs>
       
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