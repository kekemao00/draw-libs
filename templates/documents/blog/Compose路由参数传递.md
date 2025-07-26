### [Monica Code](https://monica.im/code) session transcript
 Exported: 7/24/2025, 11:45:08 AM

#### _User_

> ```kt
> // /home/xingkeqi/AndroidStudioProjects/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/ui/interests2pane/Interests2PaneViewModel.kt
> /*
>  * Copyright 2024 The Android Open Source Project
>  *
>  * Licensed under the Apache License, Version 2.0 (the "License");
>  * you may not use this file except in compliance with the License.
>  * You may obtain a copy of the License at
>  *
>  *     https://www.apache.org/licenses/LICENSE-2.0
>  *
>  * Unless required by applicable law or agreed to in writing, software
>  * distributed under the License is distributed on an "AS IS" BASIS,
>  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
>  * See the License for the specific language governing permissions and
>  * limitations under the License.
>  */
> 
> package com.google.samples.apps.nowinandroid.ui.interests2pane
> 
> import androidx.lifecycle.SavedStateHandle
> import androidx.lifecycle.ViewModel
> import androidx.navigation.toRoute
> import com.google.samples.apps.nowinandroid.feature.interests.navigation.InterestsRoute
> import dagger.hilt.android.lifecycle.HiltViewModel
> import kotlinx.coroutines.flow.StateFlow
> import javax.inject.Inject
> 
> const val TOPIC_ID_KEY = "selectedTopicId"
> 
> @HiltViewModel
> class Interests2PaneViewModel @Inject constructor(
>     private val savedStateHandle: SavedStateHandle,
> ) : ViewModel() {
> 
>     val route = savedStateHandle.toRoute<InterestsRoute>()
>     val selectedTopicId: StateFlow<String?> = savedStateHandle.getStateFlow(
>         key = TOPIC_ID_KEY,
>         initialValue = route.initialTopicId,
>     )
> 
>     fun onTopicClick(topicId: String?) {
>         savedStateHandle[TOPIC_ID_KEY] = topicId
>     }
> }
> 
> ```
> 
> ```kt
> // /home/xingkeqi/AndroidStudioProjects/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/ui/interests2pane/InterestsListDetailScreen.kt
> /*
>  * Copyright 2024 The Android Open Source Project
>  *
>  * Licensed under the Apache License, Version 2.0 (the "License");
>  * you may not use this file except in compliance with the License.
>  * You may obtain a copy of the License at
>  *
>  *     https://www.apache.org/licenses/LICENSE-2.0
>  *
>  * Unless required by applicable law or agreed to in writing, software
>  * distributed under the License is distributed on an "AS IS" BASIS,
>  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
>  * See the License for the specific language governing permissions and
>  * limitations under the License.
>  */
> 
> package com.google.samples.apps.nowinandroid.ui.interests2pane
> 
> import androidx.activity.compose.BackHandler
> import androidx.compose.animation.AnimatedContent
> import androidx.compose.foundation.interaction.MutableInteractionSource
> import androidx.compose.foundation.layout.Box
> import androidx.compose.material3.LocalMinimumInteractiveComponentSize
> import androidx.compose.material3.VerticalDragHandle
> import androidx.compose.material3.adaptive.ExperimentalMaterial3AdaptiveApi
> import androidx.compose.material3.adaptive.WindowAdaptiveInfo
> import androidx.compose.material3.adaptive.currentWindowAdaptiveInfo
> import androidx.compose.material3.adaptive.layout.AnimatedPane
> import androidx.compose.material3.adaptive.layout.ListDetailPaneScaffoldRole
> import androidx.compose.material3.adaptive.layout.PaneAdaptedValue
> import androidx.compose.material3.adaptive.layout.PaneExpansionAnchor
> import androidx.compose.material3.adaptive.layout.ThreePaneScaffoldDestinationItem
> import androidx.compose.material3.adaptive.layout.calculatePaneScaffoldDirective
> import androidx.compose.material3.adaptive.layout.defaultDragHandleSemantics
> import androidx.compose.material3.adaptive.layout.rememberPaneExpansionState
> import androidx.compose.material3.adaptive.navigation.BackNavigationBehavior
> import androidx.compose.material3.adaptive.navigation.NavigableListDetailPaneScaffold
> import androidx.compose.material3.adaptive.navigation.ThreePaneScaffoldNavigator
> import androidx.compose.material3.adaptive.navigation.ThreePaneScaffoldPredictiveBackHandler
> import androidx.compose.material3.adaptive.navigation.rememberListDetailPaneScaffoldNavigator
> import androidx.compose.runtime.Composable
> import androidx.compose.runtime.getValue
> import androidx.compose.runtime.mutableStateOf
> import androidx.compose.runtime.remember
> import androidx.compose.runtime.rememberCoroutineScope
> import androidx.compose.runtime.setValue
> import androidx.compose.ui.Modifier
> import androidx.compose.ui.draw.clipToBounds
> import androidx.compose.ui.layout.layout
> import androidx.compose.ui.unit.dp
> import androidx.hilt.navigation.compose.hiltViewModel
> import androidx.lifecycle.compose.collectAsStateWithLifecycle
> import androidx.navigation.NavGraphBuilder
> import androidx.navigation.compose.composable
> import com.google.samples.apps.nowinandroid.feature.interests.InterestsRoute
> import com.google.samples.apps.nowinandroid.feature.interests.navigation.InterestsRoute
> import com.google.samples.apps.nowinandroid.feature.topic.TopicDetailPlaceholder
> import com.google.samples.apps.nowinandroid.feature.topic.TopicScreen
> import com.google.samples.apps.nowinandroid.feature.topic.TopicViewModel
> import com.google.samples.apps.nowinandroid.feature.topic.navigation.TopicRoute
> import kotlinx.coroutines.launch
> import kotlinx.serialization.Serializable
> import kotlin.math.max
> 
> @Serializable internal object TopicPlaceholderRoute
> 
> fun NavGraphBuilder.interestsListDetailScreen() {
>     composable<InterestsRoute> {
>         InterestsListDetailScreen()
>     }
> }
> 
> @Composable
> internal fun InterestsListDetailScreen(
>     viewModel: Interests2PaneViewModel = hiltViewModel(),
>     windowAdaptiveInfo: WindowAdaptiveInfo = currentWindowAdaptiveInfo(),
> ) {
>     val selectedTopicId by viewModel.selectedTopicId.collectAsStateWithLifecycle()
>     InterestsListDetailScreen(
>         selectedTopicId = selectedTopicId,
>         onTopicClick = viewModel::onTopicClick,
>         windowAdaptiveInfo = windowAdaptiveInfo,
>     )
> }
> 
> @OptIn(ExperimentalMaterial3AdaptiveApi::class)
> @Composable
> internal fun InterestsListDetailScreen(
>     selectedTopicId: String?,
>     onTopicClick: (String) -> Unit,
>     windowAdaptiveInfo: WindowAdaptiveInfo,
> ) {
>     val listDetailNavigator = rememberListDetailPaneScaffoldNavigator(
>         scaffoldDirective = calculatePaneScaffoldDirective(windowAdaptiveInfo),
>         initialDestinationHistory = listOfNotNull(
>             ThreePaneScaffoldDestinationItem(ListDetailPaneScaffoldRole.List),
>             ThreePaneScaffoldDestinationItem<Nothing>(ListDetailPaneScaffoldRole.Detail).takeIf {
>                 selectedTopicId != null
>             },
>         ),
>     )
>     val coroutineScope = rememberCoroutineScope()
> 
>     val paneExpansionState = rememberPaneExpansionState(
>         anchors = listOf(
>             PaneExpansionAnchor.Proportion(0f),
>             PaneExpansionAnchor.Proportion(0.5f),
>             PaneExpansionAnchor.Proportion(1f),
>         ),
>     )
> 
>     ThreePaneScaffoldPredictiveBackHandler(
>         listDetailNavigator,
>         BackNavigationBehavior.PopUntilScaffoldValueChange,
>     )
>     BackHandler(
>         paneExpansionState.currentAnchor == PaneExpansionAnchor.Proportion(0f) &&
>             listDetailNavigator.isListPaneVisible() &&
>             listDetailNavigator.isDetailPaneVisible(),
>     ) {
>         coroutineScope.launch {
>             paneExpansionState.animateTo(PaneExpansionAnchor.Proportion(1f))
>         }
>     }
> 
>     var topicRoute by remember {
>         val route = selectedTopicId?.let { TopicRoute(id = it) } ?: TopicPlaceholderRoute
>         mutableStateOf(route)
>     }
> 
>     fun onTopicClickShowDetailPane(topicId: String) {
>         onTopicClick(topicId)
>         topicRoute = TopicRoute(id = topicId)
>         coroutineScope.launch {
>             listDetailNavigator.navigateTo(ListDetailPaneScaffoldRole.Detail)
>         }
>         if (paneExpansionState.currentAnchor == PaneExpansionAnchor.Proportion(1f)) {
>             coroutineScope.launch {
>                 paneExpansionState.animateTo(PaneExpansionAnchor.Proportion(0f))
>             }
>         }
>     }
> 
>     val mutableInteractionSource = remember { MutableInteractionSource() }
>     val minPaneWidth = 300.dp
> 
>     NavigableListDetailPaneScaffold(
>         navigator = listDetailNavigator,
>         listPane = {
>             AnimatedPane {
>                 Box(
>                     modifier = Modifier.clipToBounds()
>                         .layout { measurable, constraints ->
>                             val width = max(minPaneWidth.roundToPx(), constraints.maxWidth)
>                             val placeable = measurable.measure(
>                                 constraints.copy(
>                                     minWidth = minPaneWidth.roundToPx(),
>                                     maxWidth = width,
>                                 ),
>                             )
>                             layout(constraints.maxWidth, placeable.height) {
>                                 placeable.placeRelative(
>                                     x = 0,
>                                     y = 0,
>                                 )
>                             }
>                         },
>                 ) {
>                     InterestsRoute(
>                         onTopicClick = ::onTopicClickShowDetailPane,
>                         shouldHighlightSelectedTopic = listDetailNavigator.isDetailPaneVisible(),
>                     )
>                 }
>             }
>         },
>         detailPane = {
>             AnimatedPane {
>                 Box(
>                     modifier = Modifier.clipToBounds()
>                         .layout { measurable, constraints ->
>                             val width = max(minPaneWidth.roundToPx(), constraints.maxWidth)
>                             val placeable = measurable.measure(
>                                 constraints.copy(
>                                     minWidth = minPaneWidth.roundToPx(),
>                                     maxWidth = width,
>                                 ),
>                             )
>                             layout(constraints.maxWidth, placeable.height) {
>                                 placeable.placeRelative(
>                                     x = constraints.maxWidth -
>                                         max(constraints.maxWidth, placeable.width),
>                                     y = 0,
>                                 )
>                             }
>                         },
>                 ) {
>                     AnimatedContent(topicRoute) { route ->
>                         when (route) {
>                             is TopicRoute -> {
>                                 TopicScreen(
>                                     showBackButton = !listDetailNavigator.isListPaneVisible(),
>                                     onBackClick = {
>                                         coroutineScope.launch {
>                                             listDetailNavigator.navigateBack()
>                                         }
>                                     },
>                                     onTopicClick = ::onTopicClickShowDetailPane,
>                                     viewModel = hiltViewModel<TopicViewModel, TopicViewModel.Factory>(
>                                         key = route.id,
>                                     ) { factory ->
>                                         factory.create(route.id)
>                                     },
>                                 )
>                             }
>                             is TopicPlaceholderRoute -> {
>                                 TopicDetailPlaceholder()
>                             }
>                         }
>                     }
>                 }
>             }
>         },
>         paneExpansionState = paneExpansionState,
>         paneExpansionDragHandle = {
>             VerticalDragHandle(
>                 modifier = Modifier.paneExpansionDraggable(
>                     state = paneExpansionState,
>                     minTouchTargetSize = LocalMinimumInteractiveComponentSize.current,
>                     interactionSource = mutableInteractionSource,
>                     semanticsProperties = paneExpansionState.defaultDragHandleSemantics(),
>                 ),
>                 interactionSource = mutableInteractionSource,
>             )
>         },
>     )
> }
> 
> @OptIn(ExperimentalMaterial3AdaptiveApi::class)
> private fun <T> ThreePaneScaffoldNavigator<T>.isListPaneVisible(): Boolean =
>     scaffoldValue[ListDetailPaneScaffoldRole.List] == PaneAdaptedValue.Expanded
> 
> @OptIn(ExperimentalMaterial3AdaptiveApi::class)
> private fun <T> ThreePaneScaffoldNavigator<T>.isDetailPaneVisible(): Boolean =
>     scaffoldValue[ListDetailPaneScaffoldRole.Detail] == PaneAdaptedValue.Expanded
> 
> ```
> 
> ```kt
> // /home/xingkeqi/AndroidStudioProjects/nowinandroid/feature/interests/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/interests/navigation/InterestsNavigation.kt
> /*
>  * Copyright 2022 The Android Open Source Project
>  *
>  * Licensed under the Apache License, Version 2.0 (the "License");
>  * you may not use this file except in compliance with the License.
>  * You may obtain a copy of the License at
>  *
>  *     https://www.apache.org/licenses/LICENSE-2.0
>  *
>  * Unless required by applicable law or agreed to in writing, software
>  * distributed under the License is distributed on an "AS IS" BASIS,
>  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
>  * See the License for the specific language governing permissions and
>  * limitations under the License.
>  */
> 
> package com.google.samples.apps.nowinandroid.feature.interests.navigation
> 
> import androidx.navigation.NavController
> import androidx.navigation.NavOptions
> import kotlinx.serialization.Serializable
> 
> @Serializable data class InterestsRoute(
>     // The ID of the topic which will be initially selected at this destination
>     val initialTopicId: String? = null,
> )
> 
> fun NavController.navigateToInterests(
>     initialTopicId: String? = null,
>     navOptions: NavOptions? = null,
> ) {
>     navigate(route = InterestsRoute(initialTopicId), navOptions)
> }
> 
> ```
> 
> /learn-code-analogy 路由是如何传递参数的

#### _Assistant_

> # 路由参数传递：邮政系统类比
> 
> 想象一下整个应用程序是一个大型邮政系统，而路由就像是邮政配送的地址和指令。当你需要从一个屏幕（城市）传递信息到另一个屏幕时，你需要一个可靠的方式来携带数据（包裹）。
> 
> ## 📬 邮政系统的组成部分
> 
> 在我们的代码中：
> 
> 1. **地址标签** (`InterestsRoute` 类)
>    ```kotlin
>    @Serializable data class InterestsRoute(
>        val initialTopicId: String? = null,
>    )
>    ```
>    这就像一个标准化的邮政地址标签，可以包含额外信息（比如收件人的具体房间号 - `initialTopicId`）。
> 
> 2. **邮递员** (`NavController` 和它的扩展函数)
>    ```kotlin
>    fun NavController.navigateToInterests(initialTopicId: String? = null) {
>        navigate(route = InterestsRoute(initialTopicId), navOptions)
>    }
>    ```
>    这位邮递员知道如何根据地址标签将包裹送到正确的地方。
> 
> 3. **邮件室** (`SavedStateHandle` 在 ViewModel 中)
>    ```kotlin
>    val route = savedStateHandle.toRoute<InterestsRoute>()
>    val selectedTopicId = savedStateHandle.getStateFlow(
>        key = TOPIC_ID_KEY,
>        initialValue = route.initialTopicId,
>    )
>    ```
>    这是包裹到达目的地后的邮件处理室，负责接收、存储和分发包裹内容。
> 
> ## 🚚 参数传递过程
> 
> ### 第一步：准备包裹 📦
> 当用户想导航到兴趣屏幕时，应用程序会创建一个包含必要信息的"包裹"（`InterestsRoute` 实例）：
> ```kotlin
> // 相当于：准备一个标有"兴趣部门，Android 专区"的包裹
> navigateToInterests(initialTopicId = "android")
> ```
> 
> ### 第二步：邮递员配送 🚶‍♂️
> `NavController` 就像邮递员，它知道如何根据地址（路由）将包裹送到正确的地方（屏幕）。
> ```kotlin
> // 内部实现中，NavController 将路由对象序列化并配送
> navigate(route = InterestsRoute(initialTopicId), navOptions)
> ```
> 
> ### 第三步：邮件室接收 📥
> 当到达目的地（`Interests2PaneViewModel` 被创建）时，`SavedStateHandle` 扮演邮件室的角色：
> ```kotlin
> // 相当于：从包裹中提取内容
> val route = savedStateHandle.toRoute<InterestsRoute>()
> val selectedTopicId = savedStateHandle.getStateFlow(
>     key = TOPIC_ID_KEY,
>     initialValue = route.initialTopicId,
> )
> ```
> 
> ### 第四步：分发给前台人员 👨‍💼
> 最后，这些参数被传递给UI组件（Composable函数），就像邮件室将包裹内容交给前台接待人员：
> ```kotlin
> val selectedTopicId by viewModel.selectedTopicId.collectAsStateWithLifecycle()
> InterestsListDetailScreen(
>     selectedTopicId = selectedTopicId,
>     onTopicClick = viewModel::onTopicClick,
> )
> ```
> 
> ## 🔄 参数更新机制
> 
> 有趣的是，这个系统也支持"回邮"—当用户在屏幕上交互时，新的状态可以被存储：
> ```kotlin
> fun onTopicClick(topicId: String?) {
>     savedStateHandle[TOPIC_ID_KEY] = topicId
> }
> ```
> 这就像前台接待人员收到新请求后，更新了邮件室的记录系统。
> 
> ## 💡 实用见解
> 
> 1. **序列化**：`@Serializable` 注解确保路由参数可以被"打包"和"拆包"，就像邮政系统需要标准化的包装格式。
> 
> 2. **状态保存**：`SavedStateHandle` 不仅接收初始参数，还能在配置变更（如屏幕旋转）后恢复状态，就像邮件室有备份系统防止信息丢失。
> 
> 3. **单向数据流**：参数从路由流向ViewModel，再流向UI，形成清晰的数据流向，就像邮政系统中包裹的清晰配送路径。
> 
> 这种设计使得不同屏幕之间的导航和数据传递变得有条理且可预测，就像一个运作良好的邮政系统确保包裹准确送达并妥善处理。