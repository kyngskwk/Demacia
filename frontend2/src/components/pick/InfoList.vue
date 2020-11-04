<template>
    <div>
    <div>챔피언 : {{ game.champion }} | 이겼니? : {{ game.win }} | 롤 : {{ game.role }} | 라인 : {{ game.lane }}</div>
    </div>
</template>

<script>
export default {
    name: 'InfoList',
    props: {
        game: {
            type: Object
        }
    }
}
</script>

<style>

</style>