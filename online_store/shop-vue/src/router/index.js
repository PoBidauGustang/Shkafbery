import { createRouter, createWebHashHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";

const routes = [{
        path: "/",
        name: "HomePage",
        component: HomePage,
    },
    {
        path: "/about",
        name: "about",
        component: () =>
            import ("../views/AboutPage.vue"),
    },
    {
        path: "/contacts",
        name: "contacs",
        component: () =>
            import ("../views/ContactPage.vue"),
    },
    {
        path: "/photos",
        name: "photos",
        component: () =>
            import ("../views/PhotosPage.vue"),
    },
    {
        path: "/partners",
        name: "PartnerPage",
        component: () =>
            import ("../views/PartnerPage.vue"),
    },
    {
        path: "/services",
        name: "ServicesPage",
        component: () =>
            import ("../views/ServicesPage.vue"),
    },
    {
        path: "/posts",
        name: "BlogPosts",
        component: () =>
            import ("../views/PostsPage.vue"),
    },
    {
        path: "/post/:id",
        name: "article",
        component: () =>
            import ("../views/PostPageSingle.vue"),
    },
    {
        path: "/products",
        name: "List products",
        component: () =>
            import ("../views/ProductsPage.vue"),
    },
    {
        path: "/product/:id",
        name: "product",
        component: () =>
            import ("../views/ProductPageSingle.vue"),
    },
    {
        path: "/materials",
        name: "List materials",
        component: () =>
            import ("../views/MaterialsPage.vue"),
    },
    {
        path: "/material/:id",
        name: "materials",
        component: () =>
            import ("../views/MaterialPageSingle.vue"),
    },
    {
        path: "/kitchen",
        name: "kitchen",
        component: () =>
            import ("../views/KitchenPage.vue"),
    },
    {
        path: "/wardrobe",
        name: "wardrobe",
        component: () =>
            import ("../views/WardrobePage.vue"),
    },
    {
        path: "/closet",
        name: "closet",
        component: () =>
            import ("../views/ClosetPage.vue"),
    },
    {
        path: "/closet_planner",
        name: "closet planner",
        component: () =>
            import ("../views/ClosetPlannerPage.vue"),
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;